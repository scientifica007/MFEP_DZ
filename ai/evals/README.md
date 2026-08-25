# Evals — اختبارات قبول الذكاء الاصطناعي

الغرض من هذا المجلد هو مقارنة النماذج والـprompts والـpipelines على **حالات قانونية مرجعية ثابتة** قبل السماح لها بإنتاج بيانات موثوقة.

## لماذا evals إلزامية؟

قد يكون نموذج جديد أفضل لغويا لكنه أسوأ في التمييز بين الإحالة والتعديل، أو أكثر ميلا لاختلاق الحالة القانونية. لذلك لا يكفي الانطباع العام عن جودة الإجابة.

## أنواع الاختبارات

- metadata extraction
- article segmentation
- AR/FR alignment
- legal-form classification
- relation extraction
- legal-status determination
- provenance preservation
- uncertainty handling

## أخطاء مانعة للاعتماد

وجود أي خطأ من الأنواع التالية في gold cases الحساسة يستوجب رفض الترقية إلى trusted workflow حتى الإصلاح:

- hallucinated citation/reference
- false repeal
- false amendment
- fabricated legal status
- silent alteration of number/date/title
- loss of provenance
- presenting French recovery/translation as official Arabic text

## المقاييس

عند توفر عدد كاف من gold cases يمكن قياس:

- exact metadata accuracy
- article boundary precision/recall
- relation precision/recall حسب النوع
- status accuracy as-of date
- provenance completeness
- unresolved/unknown calibration

لا تعتمد نسبة مجمعة واحدة لإخفاء خطأ قانوني شديد الضرر.

## البنية

- `cases/` — المدخلات والحالات المرجعية.
- `expected/` — النتائج المقبولة/الذهبية بعد التحقق.

## عملية اعتماد نموذج أو prompt جديد

1. شغّل نفس task contracts على الحالات المرجعية.
2. قارن structured outputs بالمخرجات المتوقعة.
3. افحص الأخطاء المانعة مستقلة عن المتوسطات.
4. سجل provider/model/prompt version في run metadata.
5. إذا نجح، يمكن استخدامه في staging؛ الترقية إلى trusted تبقى خاضعة لقواعد البيانات نفسها.

## الحالة الحالية

بدأ بناء Gold Corpus فعليا من Seed Corpus 001.

الملفات الأولى:

- `cases/seed-001-relation-cases.jsonl`
- `expected/seed-001-relation-expected.jsonl`

وتتضمن أربع حالات مصدرية عالية الثقة:

1. إلغاء القانون 81-07 بواسطة القانون 18-10، مع ضرورة حفظ الحكم الانتقالي للنصوص التطبيقية القديمة.
2. تعديل وتتميم المرسوم 18-162 بواسطة المرسوم 20-340.
3. تطبيق المرسوم 12-125 للمادة 14 من القانون 08-07.
4. إلغاء القرار الوزاري المشترك المؤرخ في 24 مارس 2022 بواسطة قرار 15 فبراير 2026.

هذه الحالات تختبر خصوصا منع `false repeal`, `false amendment` والخلط بين `implements` و`references`.

لا تعتبر بقية علاقات Seed 001 Gold تلقائيا؛ العلاقة التي لم تحسم صياغتها أو لم يستكمل فحصها تبقى خارج expected outputs حتى التحقق.
