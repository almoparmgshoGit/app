from flet import *
import datetime

def main(page: Page):
    page.title = "عمل رابط واتساب"
    page.window.width = 390
    page.window.height = 740
    page.window.top = 10
    page.window.left = 960
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    
    # إعدادات الوضع الداكن
    page.bgcolor = colors.BLACK  # تحديد الخلفية إلى اللون الأسود لوضع داكن

    # شريط التطبيق العلوي
    page.appbar = AppBar(
        title=Text("عمل روابط واتساب مجانا", color=colors.WHITE),
        bgcolor='green',
        leading=Icon(icons.HOME, color=colors.WHITE),
        center_title=True,
        leading_width=80,
        actions=[
            PopupMenuButton(
                items=[
                    PopupMenuItem(text='شرح التطبيق', icon=icons.APP_BLOCKING , on_click=lambda e: page.launch_url("https://wa.me/201552825549")),
                    PopupMenuItem(text='المطورين', icon=icons.DEVELOPER_MODE_SHARP, on_click=lambda e: page.launch_url("https://wa.me/201552825549")),
                    PopupMenuItem(),
                    PopupMenuItem(text="تقييم التطبيق", icon=icons.STAR_HALF , on_click=lambda e: page.launch_url("https://wa.me/201552825549")),
                ]
            ),
        ]
    )

    # وظيفة توليد الرابط
    def generate_link(e):
        if number.value.strip():
            try:
                phone_number = int(number.value)
                message_text = message.value.strip().replace(" ", "%20") if message.value else ""
                whatsapp_link = f"https://wa.me/{phone_number}?text={message_text}" if message_text else f"https://wa.me/{phone_number}"
                
                # نسخ الرابط إلى الحافظة
                page.set_clipboard(whatsapp_link)

                # إظهار الرابط الناتج
                result_text.value = f"رابط واتساب تم إنشاؤه: {whatsapp_link}"

                # حفظ تاريخ آخر عملية
                last_generated_label.value = f"آخر عملية تم إنشاؤها: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

                # إنشاء تنبيه SnackBar
                snackbar = SnackBar(content=Text("✅ تم إنشاء الرابط ونسخه للحافظة", color=colors.WHITE), bgcolor="green")
                page.overlay.append(snackbar)
                snackbar.open = True
                page.update()
            except ValueError:
                snackbar = SnackBar(content=Text("❌ يرجى إدخال رقم صحيح!", color=colors.WHITE), bgcolor="red")
                page.overlay.append(snackbar)
                snackbar.open = True
                page.update()
        else:
            snackbar = SnackBar(content=Text("⚠️ يرجى إدخال رقم الهاتف!", color=colors.WHITE), bgcolor="red")
            page.overlay.append(snackbar)
            snackbar.open = True
            page.update()

    # صورة واتساب
    whatsapp_image = Image(
        src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg",
        width=100,
        height=100
    )

    # حقول الإدخال
    number = TextField(label="رقم الهاتف", text_align='center', prefix_icon=icons.PHONE, color=colors.WHITE, bgcolor=colors.BLACK)
    message = TextField(label="الرسالة (اختياري)", text_align='center', prefix_icon=icons.MESSAGE, color=colors.WHITE, bgcolor=colors.BLACK)

    # زر الإنشاء
    btn = ElevatedButton("إنشاء ونسخ", width=170, color=colors.WHITE, on_click=generate_link)

    # حقل لإظهار الرابط الناتج
    result_text = Text("", size=16, color=colors.WHITE, text_align="center")

    # حقل لإظهار تاريخ آخر عملية
    last_generated_label = Text("لم يتم إنشاء رابط بعد.", size=14, color=colors.WHITE, text_align="center")

    # ترتيب العناصر في الصفحة
    page.add(
        whatsapp_image,  # إضافة صورة واتساب
        number,
        message,
        btn,
        result_text,
        last_generated_label
    )

    page.update()

app(main)
