import uproot
import sys
from plothist import make_hist
from plothist import plot_hist
import matplotlib.pyplot as plt
from plothist import plot_two_hist_comparison

choice = int(sys.argv[1]) # 0 =  phsp, otherwise = isr
#variable = sys.argv[2] # name of the variable to do comparation

if choice == 0:

    df_sig_1 = uproot.open("../root_file/nbar_recoil/vpho_p_pi_n.root")["tree"].arrays(filter_name=["nbar_theta"],library="pd")
    df_sig_2 = uproot.open("../root_file/nbar_recoil/vpho_p_pi_nbg.root")["tree"].arrays(filter_name=["nb_gamma_theta"],library="pd")
    #taglio_1 = "mcISR == 1"
    title = "gamma"

'''
else: 
    df_sig_1 = uproot.open("../root_file/isr/vpho_isr_gamma_MC.root")["tree"].arrays(filter_name=["theta", "mcPDG"],library="pd")
    df_sig_2 = uproot.open("../root_file/isr/vpho_isr_gamma_REC.root")["tree"].arrays(filter_name=["theta", "genMotherPDG"],library="pd")
    taglio_1 = "mcPDG == -2112"
    title = "nbar"

taglio_2 = "genMotherPDG == 300553"
'''

# creazione di due histo riempiti con theta provenienti dai file di sopra (theta) con taglio su mcISR e genMotherPDG
bins = 50
x_range = (0., 3.)

histo_1 = make_hist(df_sig_1["nbar_theta"], bins=bins, range=x_range)
histo_2 = make_hist(df_sig_2["nb_gamma_theta"], bins=bins, range=x_range)


print(f"histo_1 is a {type(histo_1)} with {histo_1.sum()} entries")
print(f"histo_2 is a {type(histo_2)} with {histo_2.sum()} entries")

#creazione di un canvas da 1 riga e tre colonne
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(13, 4))

#metto un istogramma nel primo panello [0] e uno nel secondo pannello [1]
plot_hist(histo_1, ax=axes[0], label=r"$\bar{n}$ list", color="red",histtype = "step")
plot_hist(histo_2, ax=axes[1], label=r"$\gamma$ list", color="C0", histtype = "step")
plot_hist([histo_2, histo_1], ax=axes[2], label=[r"$\bar{n}$ list",r"$\gamma$ list"], color=["C0","red"], histtype="step")  # <--)

for ax in axes:
    ax.set_ylabel("counts []")
    ax.set_xlabel(r"$\theta$ [rad]")
    ax.legend(loc="best")

#fig.show()
fig.savefig(f"images/g_vs_n_theta.png", bbox_inches="tight")
'''
fig2, axes, ax_comparison = plot_two_hist_comparison(
    histo_2,
    histo_1,
    xlabel=r"$\theta$",
    ylabel="counts []",
    h1_label="nbar_list",
    h2_label="gamma_list",
    #comparison="efficiency"
    )

fig2.savefig(f"images/{title}_efficiency.png", bbox_inches="tight")



print(f"hist_sig bin values: {hist_sig.values()}")
print(f"hist_sig bin variances: {hist_sig.variances()}")  # plt.hist variances are not stored
print(f"hist_sig:\n{hist_sig}")
'''