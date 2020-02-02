# -*- coding: utf-8 -*-

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sns.set()

df = pd.read_csv("workouts.csv",
                 names=("date", "type", "dist", "time"),
                 index_col="date")

# groupby (check Type)
dfg = df.groupby("type").groups
for key in dfg:
    print(key, len(dfg[key]))

# plot per group
df_jog = df[df.type == "Jog"]
df_walk = df[df.type == "Walk"]
# df_jog_time = pd.to_datetime(df_jog.time, format="%H:%M:%S")

# get time
base_time = pd.to_datetime("00:00:00", format="%H:%M:%S")
df_jog_time = (pd.to_datetime(df_jog.time, format="%H:%M:%S") - base_time)
df_jog_time_sec = df_jog_time.dt.total_seconds() / 60

fig = plt.figure(figsize=(8, 6))
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)
df_jog.dist.plot(ax=ax1, grid=True, marker='o', color='r')
df_jog_time_sec.plot(ax=ax2, grid=True, marker='x', color='b')
plt.tight_layout()
plt.savefig("dist_time.png", dpi=300)
# plt.show()
plt.close()

# scatter plot
x1 = df_jog.dist.to_numpy()
x2 = df_jog_time_sec.to_numpy()
fig = plt.figure(figsize=(5, 5))
ax = fig.gca()
ax.scatter(x=x1, y=x2, marker='o', s=3, color='r')
ax.set_xlabel("distance [m]")
ax.set_ylabel("time [mins.]")
plt.tight_layout()
plt.savefig("dist_time_scatter.png", dpi=300)
# plt.show()
plt.close()