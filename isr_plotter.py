import uproot
import matplotlib.pyplot as plt

in_file1 = ["../root_file/nbar_recoil/phsp_list_gamma_MC.root",
            "../root_file/nbar_recoil/phsp_list_gamma_REC.root",
            "../root_file/nbar_recoil/phsp_list_n_MC.root",
            "../root_file/nbar_recoil/phsp_list_n_REC.root"
             ]

in_file2 = ["../root_file/isr/isr_list_gamma_MC.root",
            "../root_file/isr/isr_list_gamma_REC.root",
            "../root_file/isr/isr_list_n_MC.root",
            "../root_file/isr/isr_list_n_REC.root"
            ]

var = ["theta","theta","theta","theta"]

var_cut1 = ["genMotherPDG","genMotherPDG","genMotherPDG","genMotherPDG"]
var_cut2 = ["mcISR", "mcISR", "mcPDG", "mcPDG"]

#tagli phsp
cut1 = ["genMotherPDG == 300553","genMotherPDG == 300553", "genMotherPDG == 300553", "genMotherPDG == 300553" ] 

#tagli isr
cut2 = ["mcISR == 1", "mcISR == 1", "mcPDG == -2112", "mcPDG == -2112" ] 

title = [r"$\gamma$ list from MC", r" REC $\gamma$ list",r"$\bar{n}$ list from MC", r" REC $\bar{n}$ list"  ]

out_file = ["images/phsp_vs_isr_gammaList_MC.png", 
            "images/phsp_vs_isr_gammaList_REC.png",
            "images/phsp_vs_isr_nList_MC.png",
            "images/phsp_vs_isr_nList_REC.png"
            ]

for x in range(len(in_file1)):

    #converto il tree di output in un file panda data frame
    sig_1 = uproot.open(in_file1[x])["tree"].arrays(filter_name=[var[x], var_cut1[x]],library="pd")
    #applico il taglio desiderato
    df_sig_1 = sig_1.query(cut1[x]) 

    sig_2 = uproot.open(in_file2[x])["tree"].arrays(filter_name=[var[x], var_cut2[x]],library="pd")
    df_sig_2 = sig_2.query(cut2[x])

    """
    print(f"Number of rows (= number of candidates) before mcISR == 1: {len(df_sig)}")
    df_sig_isr = df_sig.query("mcISR == 1")
    df_sig_sec = df_sig.query("mcISR != 1")
    print(f"Number of rows (= number of candidates) due to mcISR == 1: {len(df_sig_isr)}")
    print(f"Number of rows (= number of candidates) due to mcISR != 1: {len(df_sig_sec)}")

    #numero di variabili caricate. Se non le scremo con filter_name, le carica tutte
    #print(f"Number of columns (= number of variables): {len(df_sig_.columns)}")
    """

    fig, ax = plt.subplots() #comando per associare una canvas (fig) e degli assi (ax) pescndo dal modulo plt (matplotlib.pyplot)

    ax.hist(df_sig_1[var[x]], bins=50, range=(0., 3.5), label="PHSP",  color="blue",)  #lavoro su ax e creo l'hihsto dei gamma secondari
    ax.hist(df_sig_2[var[x]], bins=50, range=(0., 3.5), label="ISR",  color="red",)

    ax.set_xlabel(r"$\theta$ [rad]")
    ax.set_ylabel("Counts []")
    ax.set_title(title[x])
    ax.legend()

    # plt.hist(df_sig["theta"])

    fig.savefig(out_file[x], bbox_inches="tight") #salvo la figura