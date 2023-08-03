import seaborn as sns
survivalrate=sns.countplot(x="survived",hue="pclass",data=titanic)
survivalrate.set_xticklabels(['not survived','survived'])
survivalrate.set(xlabel="survival",ylabel="counts",title="survival rate differ by passenger class")
