#for since 2560 onward
# ref https://www.rd.go.th/59670.html
import pandas as pd
import numpy as np
NetIncomeData =[
     [0.0, 150000.0, 150000.0, 0.05, 0, 0],
     [150000.01, 300000.0, 150000.0, 0.05, 7500.0, 7500.0],
     [300000.01, 500000.0, 200000.0, 0.1, 20000.0, 27500.0],
     [500000.01, 750000.0,  250000.0, 0.15,  37500.0,  65000.0],
     [750000.01, 1000000.0, 250000.0, 0.2, 50000.0, 115000.0],
     [1000000.01, 2000000.0,  1000000.0, 0.25, 250000.0, 365000.0],
     [2000000.01,  5000000.0,  3000000.0, 0.3, 900000.0, 1265000.0],
     [5000000.01, 9.999999*10**10, np.nan, 0.35, 0]
 ]

incomedata = pd.DataFrame(NetIncomeData, columns=['Lower','High','Maxinterval','Rate','Maxtaxinterval','Accumtax'])

def cal_pit_2560(netincome)->float:
    pittax = lambda ac, ri, cr : (ri*cr)+ac if ~np.isnan(ac) else 0
    tax = incomedata[(incomedata['Lower']<=netincome) & (netincome<=incomedata['High'])]
    if np.isnan(incomedata[incomedata['High']<=netincome]['Accumtax'].max()) :
        return 0
    else :
        return pittax(incomedata[incomedata['High']<=netincome]['Accumtax'].max(), (netincome - int(tax['Lower'])), tax['Rate'].sum()*(~np.isnan(incomedata[incomedata['High']<=netincome]['Accumtax'].max())))

def main():
    income=1340000.0
    cal_pit_2560(net_income)

if __name__ == "__main__":
    main()