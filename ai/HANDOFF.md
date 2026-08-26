# MFEP_DZ — Handoff

آخر تحديث: 2026-08-26

هذا الملف يعطي أي Agent جديد حالة المشروع الحالية دون الاعتماد على محادثة سابقة.

## المرحلة الحالية

`human_machine_packages_complete_transcription_validation_in_progress`

يوجد 12 سجلا قانونيا في دورة staging/validation، وقد اكتملت هجرتها جميعا إلى حزم دائمة تحت `corpus/texts/` تجمع القراءة البشرية والاستدعاء الآلي. تبقى صفة `staging` مرتبطة بدرجة التحقق، لا بمكان الملف.

## قاعدة التخزين: لا PDF في Git

- لا تحفظ ملفات PDF أو صور صفحات الجريدة الرسمية داخل المستودع.
- `.gitignore` يمنع `*.pdf` و`*.PDF`.
- `scripts/validate_repository.py` يعتبر وجود PDF داخل شجرة المستودع خطأ.
- تحفظ روابط JORADP ورقم الجريدة والصفحات ومحددات اللغة في `sources/sources.yml`.
- إذا احتاج workflow إلى PDF فإنه ينزل مؤقتا، يستخرج النص، ثم يحذف الملف.
- `scripts/materialize_joradp_text.py` يطبق هذا النمط.
- راجع `docs/STORAGE_POLICY.md`.

## نموذج Human + Machine الدائم

لكل نص:

```text
corpus/texts/<TEXT_ID>/
├── README.md
├── record.yml
├── text/
│   ├── ar.md
│   └── fr.md
├── data/
│   └── articles.jsonl
└── sources/
    └── sources.yml
```

- `README.md`: واجهة الباحث/الإنسان.
- `record.yml`: metadata والتصنيف والحالة والتحقق.
- `articles.jsonl`: عنونة واستدعاء المواد للآلة وحالة كل transcription.
- `text/ar.md`, `text/fr.md`: transcription نصية مع حالة صريحة.
- `sources.yml`: source of evidence ولا يحتوي binary.

## حالة الهجرة

تمت هجرة السجلات الـ12 الحالية كلها، مع تحديث metadata إلى المسارات الجديدة وحذف ملفات record القديمة من `corpus/staging/seed-*` حتى لا توجد نسختان دائمتان للحقيقة.

الفهرس البشري: `corpus/INDEX.md`.

## أول متن كامل داخل المستودع: DZ-LAW-2008-007

القانون 08-07 هو أول نص يكتمل داخليا على مستوى المتن:

- `text/fr.md`: النص الفرنسي الكامل من التأشيرات إلى المادة 32، حالة `verified` بعد مطابقة طبقة النص مع الصفحات الرسمية 4–6.
- `text/ar.md`: النص العربي الكامل من التأشيرات إلى المادة 32، حالة `transcribed` بعد النقل من الصفحات الرسمية 4–7 والمقابلة الفرنسية؛ يحتاج مرور تدقيق ثانيا قبل `verified`.
- `data/articles.jsonl`: 32 معرف مادة مستقرا من `#art-1` إلى `#art-32`، وكل سجل يحمل page locators وحالة النسختين ومسار النص.
- `record.yml`: يصرح صراحة بأن الفرنسية متحققة والعربية منقولة وغير متحققة نهائيا.

يمكن الآن للإنسان والـAgent قراءة القانون 08-07 كاملا من داخل Git دون الاعتماد التشغيلي على PDF، مع بقاء JORADP المرجع القانوني الأصلي.

## قاعدة استعمال المتن

الحالات المستخدمة تشمل:

- `source_resolution_pending`
- `source_locator_only`
- `transcription_pending`
- `transcribed`
- `verified`

لا يجوز لأي Agent وصف transcription بأنها موثقة نهائيا إلا عند `verified`. يمكن استخدام `transcribed` للبحث والمقابلة، لكن يجب إظهار درجة التحقق عند النقل الحرفي أو الحكم على اختلاف لغوي.

## حالة corpus القانونية الحالية

- Graph أولي تحت `graph/staging/`.
- metadata indexes تحت `metadata/staging/` وتشير إلى `corpus/texts/`.
- discovery queue تحت `metadata/discovery-queue.jsonl`.
- Gold Evals أولية للعلاقات القانونية.
- ontology `0.2-draft`.
- 12 حزمة Human + Machine تحت `corpus/texts/`.
- أول transcription كاملة: `DZ-LAW-2008-007`.

## أهم نتائج التصميم

1. Locator النشر مستقل لكل لغة.
2. لا يفضل تضمين القطاع في Canonical ID قبل تثبيت السياسة.
3. الأعمال غير المرقمة تحتاج تاريخ + discriminator؛ لا نخترع أرقاما.
4. relation verification مستقل عن legal-status verification.
5. `status.as_of` ليس `repeal_date`.
6. `interministerial_order` هو المفتاح القانوني للقرار الوزاري المشترك.
7. `provides_for_implementing_act` يختلف عن `enabling_legislation`.
8. النصوص الأفقية تدخل بحسب أثرها على القطاع.
9. النجاح البنيوي في Validator لا يثبت صحة الحكم القانوني.
10. الإنسان والآلة يصلان إلى الكيان نفسه عبر واجهتين، وليس عبر قاعدتي حقيقة منفصلتين.
11. PDF مصدر خارجي لا artifact دائم للمشروع.
12. transcription يمكن أن تكون مكتملة لغويا مع اختلاف درجة التحقق بين العربية والفرنسية؛ لا نفرض status واحدا على الكيان كله.
13. `articles.jsonl` يفهرس النص ولا يصبح مصدرا مستقلا عن ملفات `text/`؛ الهدف تجنب ازدواج النص الحرفي يدويا.

## العمل التالي ذو الأولوية

1. إجراء المرور الثاني على العربية للقانون 08-07 وترقيتها إلى `verified` إذا لم تظهر فروق.
2. تطبيق نفس materialization والتحقق على النصوص التالية حسب القيمة القانونية وحجم النص، بدءا بالنصوص التطبيقية المرتبطة مباشرة بمواد 08-07 ثم القانون 18-10.
3. توسيع Validator للتحقق من اتساق `articles.jsonl` مع ملفات transcription وحالات اللغات.
4. إدخال سلسلة تعديلات القانون 81-07 قبل إلغائه: 90-34، 2000-01، 14-09.
5. إدخال المرسوم 81-392 والنص التطبيقي لسنة 2020 الذي ألغاه.
6. إدخال سلسلة تعديلات 22-70: 22-254، 23-60، 26-87.
7. حسم علاقة 14-140 بالقانون 08-07 على مستوى المادة.
8. توسيع Gold Evals لتشمل transcription/AR-FR alignment والحالة القانونية.
9. اختبار أنواع لم تغط بعد: أمر، مرسوم رئاسي/معاهدة، قرار فردي، تعليمة/منشور، إلغاء جزئي.
10. بعد نضج الحالات تثبيت `legal-text.schema.json` v1.

## ملفات الاستئناف الأساسية

- `corpus/INDEX.md`
- `corpus/texts/README.md`
- `corpus/texts/DZ-LAW-2008-007/README.md`
- `corpus/texts/DZ-LAW-2008-007/text/ar.md`
- `corpus/texts/DZ-LAW-2008-007/text/fr.md`
- `corpus/texts/DZ-LAW-2008-007/data/articles.jsonl`
- `docs/STORAGE_POLICY.md`
- `docs/HUMAN_MACHINE_CORPUS.md`
- `metadata/staging/seed-001.jsonl`
- `metadata/staging/seed-002-dependencies.jsonl`
- `graph/staging/seed-001-relations.jsonl`
- `graph/staging/seed-002-relations.jsonl`
- `metadata/discovery-queue.jsonl`
- `ontology/core.yml`
- `scripts/materialize_joradp_text.py`
- `scripts/validate_repository.py`

## قاعدة الاستئناف

لا توسع corpus لمجرد زيادة العدد. الأولوية لتحويل المصادر الرسمية إلى transcription نصية خفيفة ومراجعة، مع حفظ صريح لدرجة الثقة وعدم إدخال أي PDF. بعد اكتمال أول نموذج 08-07، يطبق نفس النمط على النصوص المرتبطة به مباشرة قبل التوسع التاريخي الواسع.
