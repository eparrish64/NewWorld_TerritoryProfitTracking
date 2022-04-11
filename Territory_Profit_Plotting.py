import pandas as pd
import matplotlib.pyplot as plt

def main():
	"""
	import data from csv file, plot multi line graph, and save it.
	"""

	df = pd.read_csv("Ohono_Territories.csv")

	print(df.head())

	small_df = df[["Territory","3","4","2","1"]]
	small_df["4"]=small_df["4"].astype(float)
	small_df["3"]=small_df["3"].astype(float)
	small_df["2"]=small_df["2"].astype(float)
	small_df["1"]=small_df["1"].astype(float)
	print(small_df.head())
	small_df=small_df.pivot_table(columns="Territory")
	small_df = small_df[[
	# "Restless Shores", 
	"Monarch's Bluffs",
	 # "Reekwater", 
	 "Weaver's Fen", 
	 "Cutlass Keys", 
	 "Mourningdale", 
	 "First Light", 
	 # "Brightwood", 
	 "Everfall", 
	 # "Windsward", 
	 "Ebonscale Reach",
	 ]]
	print(small_df.head())
	ax = small_df.plot(ylim=(0,2100000), lw=2, marker='.', markersize=10, title='Profits by Territory', grid=True)
	# ax.set(xlabel="Week", ylabel="Profit in Coin")
	ax.set_ylabel("Profit in Coin", labelpad=0)
	ax.set_xlabel("Week")
	plt.legend(ncol=2)
	ax.get_figure().savefig("Profits_Non_Yellow.png")
	return 0

if __name__ == "__main__":
	main()