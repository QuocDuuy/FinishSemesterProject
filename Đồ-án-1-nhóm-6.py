#!/usr/bin/env python
# coding: utf-8

# In[4]:


def tensv(): #hàm nhập tensv
    while True: #khi nó đúng
        hoten = input() #nhập họ tên vào
        n = hoten.split(' ') #tách tên thành các chuỗi nhỏ
        for i in range(len(n)): #cho i chạy trong từng chuỗi nhỏ của n
            if (n[i].isdigit() or not n[i].isalpha()): #i chạy xét điều kiện
                print("Mời nhập lại họ tên: ")
                break # phá khỏi vòng if
        else:
            break
    m =' '.join(n) #gộp cái lst đã khai báo ở trên
    return 'Họ tên: ' + m #trả giá trị 


# In[2]:


# while True:
#     name = input("Hãy Nhập tên: ")
#     n = name.split(' ')
#     for i in range(len(n)):
#         if(not (n[i].isalpha()) or (n[i].isdigit())):
#             print("hÃY NHẬP Lại")
#             break
#     else:
#         print("Ho ten: ", ' '.join(n))
#         break


# In[5]:


from datetime import date #thêm thư viện date từ module datetime
def ntns(): #hàm nhập ntns
    while True: #khi đúng
        ngay = int(input("Mời nhập ngày: ")) #nhập ngày
        if (ngay not in range(1,32)): #nếu không nằm trong khoảng từ 1 đến 31 ngày thì mời nhập lại
            print("Mời nhập lại ngày: ") 
            continue #tiếp tục chạy 
        else:
            thang = int(input("Nhập tháng: ")) #nhập tháng
            if(thang not in range(1,13)): #nếu không nằm trong khoảng từ tháng 1 đến tháng 12 thì mời nhập lại
                print("Mời nhập lại tháng: ")
                continue #tiếp tục chạy
            else:
                nam = int(input("Nhập năm: ")) #nhập năm
                if (nam not in range(1000,3000)): #nếu số năm không nằm trong khoảng từ năm 1000 đến năm 3000 thì mời nhập lại
                    print("Mời nhập lại năm: ")
                    continue #tiếp tục chạy
                else:
                    return 'Ngày tháng năm sinh: ' + str(ngay) + '/' + str(thang) + '/' + str(nam) #trả lại giá trị ngày tháng năm
                    break #phá vòng if


# In[6]:


def mssv(): #hàm nhập mssv
    while True: #nếu đúng
        ID = input("Mời nhập MSSV: ") #nhập mssv
        if (not ID.isdigit() or len(ID) != 10): #xét điều kiện nếu mssv không phải là số hoặc độ dài của mssv khác 10 thì mời nhập lại
            print("Mời nhập lại MSSV: ")
            continue #tiếp tục chạy
        else:
            return 'Mã số sinh viên: ' + ID #trả lại giá trị 
            break


# In[7]:


def NhapDauVao(): #hàm nhập đầu vào
    print("\nThông tin sinh viên: ")
    return tensv() + '\n' + ntns() + '\n' + mssv()
sv = NhapDauVao()
print(sv)


# In[8]:


monhoc = ["Điểm_kết_thúc_học_phần A", "Điểm_kết_thúc_học_phần B", "Điểm_kết_thúc_học_phần C", "Điểm_kết_thúc_học_phần D", "Điểm_kết_thúc_học_phần E"]
import random
tongdkt = 0
for i in range(len(monhoc)):
    d30 = random.randint(0, 10)
    d70 = random.randint(0, 10)
    dkt = round(d30*(30/100) + d70*(70/100))
    if(dkt >= 5):
        print(monhoc[i], ":", dkt, "Dau")
    else:       
        print(monhoc[i], ":", dkt, "Rot") 
    số_tín_chỉ_mỗi_môn = 3
    tổng_số_tín_chỉ = 15 
    tongdkt += dkt
#############################################
Điểm_cuối_kỳ = (tongdkt * số_tín_chỉ_mỗi_môn ) / tổng_số_tín_chỉ
print(Điểm_cuối_kỳ)
if Điểm_cuối_kỳ >= 9:
    print ("Hs giỏi")
elif Điểm_cuối_kỳ >= 7:
    print ("hs khá")
elif Điểm_cuối_kỳ >= 5:
    print ("hoc sinh tb")
else :
    print ("học sinh yếu")

