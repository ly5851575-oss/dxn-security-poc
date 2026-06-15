# AI Tools — Defensive Security Pack

حزمة أدوات دفاعية بسيطة للعمل من Termux أو Linux داخل الأنظمة التي تملكها أو لديك تصريح مكتوب لفحصها.

## الملفات المرفوعة

- `scanner.py`: فحص منافذ TCP محددة فقط، بحد أقصى 100 منفذ في كل تشغيل.
- `encoding_demo.py`: ترميز وفك ترميز نصوص Base64 لأغراض تعليمية، ولا يولّد أوامر shell أو reverse shell.

## التثبيت في Termux

```bash
pkg update -y
pkg install -y git python

git clone https://github.com/ly5851575-oss/dxn-security-poc.git
cd dxn-security-poc/ai_tools
```

## الاستخدام

### فحص منافذ مصرح بها

```bash
python scanner.py 127.0.0.1 22 80 443
```

### ترميز وفك ترميز نص

```bash
python encoding_demo.py encode "hello"
python encoding_demo.py decode "aGVsbG8="
```

## ملاحظة أمنية

لم يتم تضمين مولّد reverse shell أو أداة auto-exploit أو أي ملف يرسل أوامر إلى خادم بعيد. استخدم الأدوات فقط على أصول تملكها أو ضمن نطاق اختبار مصرح به كتابةً.
