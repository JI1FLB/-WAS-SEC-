#------------------------------
#
# 広島WASコンテスト　Secファイル作成プログラム
#
#

#       定数定義

#       全グリッドロケータを作成する場合の定数定義
#
#       Grid1 = "ABCDEFGHIJKLMNOPQR"
#       Grid2 = "ABCDEFGHIJKLMNOPQR"
#

Grid1 = "PQ"
Grid2 = "LMN"

i=0
j=0
n=0
m=0


sec_file = open( "WAS.sec" ,"w", encoding="utf-8")

sec_file.write("Type=WAS  SubType="+"\n")
sec_file.write("35001"+"\n")
sec_file.write("35007"+"\n")
sec_file.write("35008"+"\n")
sec_file.write("35010"+"\n")
sec_file.write("350101"+"\n")
sec_file.write("350102"+"\n")
sec_file.write("350103"+"\n")
sec_file.write("350104"+"\n")
sec_file.write("350105"+"\n")
sec_file.write("350106"+"\n")
sec_file.write("350107"+"\n")
sec_file.write("350108"+"\n")
sec_file.write("35016"+"\n")
sec_file.write("3502"+"\n")
sec_file.write("3503"+"\n")
sec_file.write("3504"+"\n")
sec_file.write("3505"+"\n")
sec_file.write("3508"+"\n")
sec_file.write("3509"+"\n")
sec_file.write("3510"+"\n")
sec_file.write("3511"+"\n")
sec_file.write("3512"+"\n")
sec_file.write("3513"+"\n")
sec_file.write("3514"+"\n")
sec_file.write("3515"+"\n")
sec_file.write("3516"+"\n")


#       全グリッドロケータを作成する場合の設定
#
#       for i in range(0,18):
#       	for j in range(0,18):

for i in range(0,2):
	for j in range(0,3):
		for n in range(0,10):
			for m in range(0,10):
				sec_file.write(Grid1[i]+Grid2[j]+str(n)+str(m)+"\n")
	
sec_file.close()
