plt.pie(x=data['country'].value_counts()[:10],labels=data['country'].value_counts().index[:10])
plt.savefig('/home/doc-bd-a1/vis.png')