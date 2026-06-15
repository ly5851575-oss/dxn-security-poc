# AI Tools — Defensive Security Pack

حزمة أدوات دفاعية بسيطة للعمل من Termux أو Linux داخل الأنظمة التي تملكها أو لديك تصريح مكتوب لفحصها.

## الملفات

- `scanner.py`: فحص منافذ محددة فقط، بحد أقصى 100 منفذ في كل تشغيل.
- `encoding_demo.py`: ترميز وفك ترميز نصوص Base64 لأغراض تعليمية، ولا يولّد أوامر shell.
- `http_check.sh`: التحقق من حالة HTTP والرؤوس الأمنية بدون إرسال أوامر إلى الخادم.
- `install_termux.sh`: تثبيت المتطلبات الأساسية في Termux.

## التثبيت في Termux

```bash
pkg update -y
pkg install -y git python curl

git clone https://github.com/ly5851575-oss/dxn-security-poc.git
cd dxn-security-poc/ai_tools
chmod +x http_check.sh install_termux.sh
./install_termux.sh
```

## أمثلة الاستخدام

### فحص منافذ مصرح بها

```bash
python scanner.py 127.0.0.1 22 80 443
```

### ترميز نص

```bash
python encoding_demo.py encode "hello"
python encoding_demo.py decode "aGVsbG8="
```

### فحص HTTP دفاعي

```bash
./http_check.sh https://example.com
```

## نطاق الاستخدام

هذه الأدوات لا تتضمن reverse shell أو auto-exploit أو تنفيذ أوامر عن بعد. استخدمها فقط على أصول تملكها أو ضمن نطاق اختبار مصرح به كتابةً.
