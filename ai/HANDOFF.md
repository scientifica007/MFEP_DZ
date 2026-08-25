# MFEP_DZ — Handoff

آخر تحديث: 2026-08-25

هذا الملف يعطي أي Agent جديد حالة المشروع الحالية دون الاعتماد على محادثة سابقة.

## المرحلة الحالية

`seed_corpus_staging_validation_and_human_machine_migration`

يوجد 12 سجلا قانونيا في دورة staging/validation. بدأ تحويل السجلات من ملفات metadata منفردة إلى حزم دائمة تجمع القراءة البشرية والاستدعاء الآلي. أول نص مهاجر فعليا هو `DZ-LAW-2008-007`.

## القرار الجديد الحاسم: لا PDF في Git

- لا تحفظ ملفات PDF أو صور صفحات الجريدة الرسمية داخل المستودع.
- `.gitignore` يمنع `*.pdf` و`*.PDF`.
- `scripts/validate_repository.py` يعتبر وجود PDF داخل شجرة المستودع خطأ.
- تحفظ روابط JORADP ورقم الجريدة والصفحات ومحددات اللغة في `sources/sources.yml`.
- إذا احتاج workflow إلى PDF فإنه ينزل مؤقتا، يستخرج النص، ثم يحذف الملف.
- راجع `docs/STORAGE_POLICY.md`.

## نموذج Human + Machine الدائم

لكل نص بعد الهجرة:

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

### معنى الملفات

- `README.md`: واجهة الباحث/الإنسان.
- `record.yml`: metadata والتصنيف والحالة والتحقق.
- `articles.jsonl`: عنونة واستدعاء المواد للآلة.
- `text/ar.md`, `text/fr.md`: transcription نصية؛ يجب قراءة `status` قبل اعتبارها مكتملة.
- `sources.yml`: source of evidence ولا يحتوي binary.

## أول هجرة: القانون 08-07

المسار: `corpus/texts/DZ-LAW-2008-007/`.

المكتمل:

- واجهة بشرية كاملة من حيث البطاقة وخريطة المواد والعلاقات المعروفة؛
- سجل `record.yml`؛
- فهرس 32 مادة في `data/articles.jsonl` مع page locators AR/FR؛
- source manifest؛
- ملفات اللغة وحالة transcription؛
- تحديث metadata ليشير إلى المسار الجديد؛
- حذف ملف السجل القديم المكرر من `corpus/staging/seed-001/`.

**تنبيه:** المتن الكامل العربي والفرنسي داخل ملفات `text/` لم يعتمد بعد كـ`verified transcription`. وجود source links وفهرس المواد لا يساوي وجود متن داخلي متحقق.

## أدوات جديدة

- `scripts/materialize_joradp_text.py`: ينزل PDF مؤقتا ويستخرج النص بواسطة `pdftotext` ثم يحذف PDF.
- `scripts/validate_repository.py`: validation بنيوي + حظر PDF.

## حالة corpus السابقة المستمرة

- 12 سجلا قانونيا في دورة staging/validation.
- Graph أولي تحت `graph/staging/`.
- metadata indexes تحت `metadata/staging/`.
- discovery queue تحت `metadata/discovery-queue.jsonl`.
- Gold Evals أولية للعلاقات القانونية.
- ontology `0.2-draft`.

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
10. النص القانوني يجب أن يكون قابلا للقراءة للإنسان والاستدعاء للآلة من نفس الحزمة، دون PDF داخل Git.

## العمل التالي ذو الأولوية

1. إتمام transcription المراجع للقانون 08-07، بدءا بالفرنسية ثم مقابلة العربية وتصحيحها.
2. بعد نجاح 08-07، هجرة النصوص الـ11 الباقية إلى `corpus/texts/` دون ازدواج records.
3. توسيع `articles.jsonl` ليحمل text payload فقط عندما يعتمد transcription الخاص بالمادة.
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
- `docs/STORAGE_POLICY.md`
- `metadata/staging/seed-001.jsonl`
- `metadata/staging/seed-002-dependencies.jsonl`
- `graph/staging/seed-001-relations.jsonl`
- `graph/staging/seed-002-relations.jsonl`
- `metadata/discovery-queue.jsonl`
- `ontology/core.yml`
- `scripts/materialize_joradp_text.py`
- `scripts/validate_repository.py`

## قاعدة الاستئناف

لا توسع corpus لمجرد زيادة العدد. الأولوية الآن لإثبات أن حزمة Human + Machine قابلة للصيانة والاستدعاء على نص حقيقي، ثم تعميمها. لا يوصف النص الكامل بأنه مخزن داخليا إلا إذا كانت transcription ذات حالة معلنة ومتحققة.
