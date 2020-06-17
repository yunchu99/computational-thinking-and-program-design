step1=input("您好，我是點餐機器人Bella878，歡迎光臨master donuts，今天有蜜糖波堤和豆香波堤，您要點什麼呢?")
    
while True:
    step2=input("好的，有需要加購飲料嗎(有/沒有)?")
    if step2=="有":        
        while True:
            step3=input("有紅茶和鮮奶茶，請問你需要什麼?")
            if step3=="紅茶" or step3=="鮮奶茶":                
                while True:
                    step4=input("好的，甜度需要調整嗎(無糖/微糖/半糖/少糖/全糖)?")
                    if step4=="無糖" or step4=="微糖" or step4=="半糖" or step4=="少糖" or step4=="全糖":
                        while True:
                            step5=input("好的，冰塊需要調整嗎(完全去冰/去冰/微冰/少冰/正常冰)?")
                        
                            if step5=="完全去冰" or step5=="去冰" or step5=="微冰" or step5=="少冰" or step5=="正常冰":
                                step2="您加購的飲料為:"+step3+" "+step4+" "+step5+"\n"
                                break
                            else:
                                print("無此選項，請重新輸入")
                        break
                    else:
                        print("無此選項，請重新輸入")
                break
            else:
                print("無此選項，請重新輸入")
        break
    elif step2=="沒有":
        step2="沒有加購飲料"
        break
    else:
        print("無此選項，請重新輸入")
        
while True:
    step6=input("好的，需要紙巾嗎(要/不要)?")
    if step6=="要":
        step6="需要紙巾"
        break
    elif step6=="不要":
        step6="不需要紙巾"
        break
    else:
        print("無此選項，請重新輸入")

while True:
    step7=input("好的，需要紙袋嗎(要/不要)?")
    if step7=="要":
        step7="需要紙袋"
        break
    elif step7=="不要":
        step7="不需要紙袋"
        break
    else:
        print("無此選項，請重新輸入")

while True:
    step8=input("好的，請問需要統編嗎(要/不要)?")
    if step8=="要":        
        while True:
            step8=input("請輸入您的統編:")
            if len(step8)==8:
                step9="統編號碼為:"+step8
                break
            else:
                print("統編長度不正確，請重新輸入")            
        break
    elif step8=="不要":
        step9="不需要統編"
        break
    else:
        print("無此選項，請重新輸入")

while True:
    step10=input("好的，請問需要載具嗎(要/不要)?")
    if step10=="要":
        step10="需要載具"
        break
    elif step10=="不要":
        step10="不需要載具"
        break
    else:
        print("無此選項，請重新輸入")
print("好的，您點的餐點為:\n"+step1+"\n"+step2+step6+"\n"+step7+"\n"+step9+"\n"+step10)
print("刷卡請於右下方感應，現金請至櫃台結帳，希望很快能再度為您服務")
