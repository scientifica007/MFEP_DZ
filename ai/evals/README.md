# Evals — اختبارات قبول الذكاء الاصطناعي

الغرض من هذا المجلد هو مقارنة النماذج والـprompts والـpipelines على **حالات قانونية مرجعية ثابتة** قبل السماح لها بإنتاج بيانات موثوقة.

## لماذا evals إلزامية؟

قد يكون نموذج جديد أفضل لغويا لكنه أسوأ في التمييز بين الإحالة والتعديل، أو أكثر ميلا لاختلاق الحالة القانونية أو بناء نص موحد بطريقة تغير النص الأصلي. لذلك لا يكفي الانطباع العام عن جودة الإجابة.

## أنواع الاختبارات

- metadata extraction
- article segmentation
- AR/FR alignment
- legal-form classification
- relation extraction
- legal-status determination
- provenance preservation
- uncertainty handling
- amendment mapping
- dated legal consolidation
- unresolved implementing-act detection
- multi-repeal extraction

## أخطاء مانعة للاعتماد

وجود أي خطأ من الأنواع التالية في gold cases الحساسة يستوجب رفض الترقية إلى trusted workflow حتى الإصلاح:

- hallucinated citation/reference
- false repeal
- false amendment
- fabricated legal status
- silent alteration of number/date/title
- loss of provenance
- presenting French recovery/translation as official Arabic text
- silently overwriting an original text with an amendment
- treating `sans changement / بدون تغيير` as permission to invent text
- presenting a project-generated consolidated version as an official publication
- presenting a dated consolidation as current law without forward search
- inventing a ministerial order number/date when only an implementing-act slot is known
- inventing transitional survival where a repeal article contains none

## المقاييس

عند توفر عدد كاف من gold cases يمكن قياس:

- exact metadata accuracy
- article boundary precision/recall
- relation precision/recall حسب النوع
- status accuracy as-of date
- provenance completeness
- unresolved/unknown calibration
- amendment-target accuracy
- consolidation provenance completeness

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

### علاقات قانونية — Seed

- `cases/seed-001-relation-cases.jsonl`
- `expected/seed-001-relation-expected.jsonl`

تشمل الإلغاء، التعديل، التطبيق، الإضافة والأثر الانتقالي.

### علاقات التوسع الموضوعي — 24-74

- `cases/sector-expansion-relation-cases.jsonl`
- `expected/sector-expansion-relation-expected.jsonl`

وتختبر أربع حالات جديدة:

1. المادة 1 من 24-74 باعتبارها `implements` صريحة للمادة 20 من القانون 08-07؛
2. المادة 19 باعتبارها `applies` للمرسوم 16-282 في نظام تتويج المعابر والحركية المهنية؛
3. المادة 23 كحالة **multi-repeal** لثلاثة مراسيم دون اختراع أثر انتقالي غير منصوص عليه؛
4. المواد 13 و14 و22 كحالات `provides_for_implementing_act` منفصلة، مع منع اختراع رقم أو تاريخ القرار قبل اكتشافه.

### Consolidation

أضيفت أول حالات Gold لبناء نسخة بحثية موحدة مؤرخة من سلسلة 18-162 ← 20-340:

- `cases/consolidation-cases.jsonl`
- `expected/consolidation-expected.jsonl`

وتختبر أربع نقاط عالية الحساسية:

1. **المادة 16:** التفريق بين صيغة 2018 الأصلية وصيغة 2020 المعدلة، وعدم إسقاط ملاحظة التحقق العربية المفتوحة.
2. **المادة 35 مكرر:** إدراج المادة الجديدة بعد 35 وقبل 36 دون استبدال أو إعادة ترقيم مواد أخرى.
3. **المادة 41:** اعتماد مهلة الأربع سنوات واستثناء 35 مكرر بدل إبقاء مهلة السنة الأصلية.
4. **هوية النسخة:** وصف الناتج بأنه `research_consolidated_version` بتاريخ قطع محدد، لا نصا رسميا ولا الحالة القانونية الحالية بلا forward search.

هذه الاختبارات تجعل تغيير نموذج الذكاء الاصطناعي آمنًا بدرجة أكبر عند الانتقال من استخراج العلاقات إلى إعادة بناء نص قانوني مركب أو اكتشاف نصوص تطبيقية غير محلولة.

لا تعتبر أي علاقة أو consolidation Gold تلقائيا؛ الموضع الذي لم يحسم مصدره أو تحققُه يبقى موسومًا ولا يُحوَّل إلى expected output واثق.
