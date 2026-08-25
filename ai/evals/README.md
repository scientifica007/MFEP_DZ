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

الإطار موجود، لكن gold corpus لم يُبن بعد. سيُنشأ من أول 5–10 نصوص ممثلة بعد التحقق اليدوي/المصدري منها.