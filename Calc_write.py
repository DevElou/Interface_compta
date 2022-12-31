import Calc_read as read


def write_solde(open_file,Line):
    open_file.loc[Line, ['SOLDE']] = read.calc_solde(open_file,Line)

def save(open_file,name):
    open_file.to_excel(f"{name}.xlsx")

def add_line(open_file,cat,deb,cred):
    max_ind = open_file.index[-1]
    open_file.loc[max_ind+1] = [cat,deb,cred,0]





add_line(read.data,"Alimentation",0,10)
write_solde(read.data,read.data.index[-1])
print(read.data)



