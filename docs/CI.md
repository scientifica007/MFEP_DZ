# CI — التحقق المستمر من سلامة المستودع

## الغرض

يستخدم المشروع GitHub Actions لتشغيل التحقق البنيوي الحتمي على النسخة الفعلية من المستودع، بدلا من الاعتماد على قدرة بيئة محادثة أو جهاز محلي على استنساخ GitHub.

الـWorkflow المعتمد:

`.github/workflows/validate-repository.yml`

## متى يعمل؟

يعمل تلقائيا عند:

- كل `push` إلى `main`؛
- كل Pull Request؛
- التشغيل اليدوي عبر `workflow_dispatch`.

## ما الذي يختبره؟

الـjob الحالي اسمه:

`Deterministic corpus validation`

ويشغل بالتسلسل:

```bash
python scripts/test_joradp_resolver.py
python scripts/validate_repository.py .
```

اختبارات JORADP هنا **غير شبكية**: تختبر منطق resolver فقط ولا تطلب موقع JORADP.

الـValidator يفحص، من بين أمور أخرى:

- منع أي PDF داخل Git؛
- سلامة JSONL؛
- تطابق vocabulary مع Ontology؛
- وجود `record_path`؛
- عدم تكرار معرفات النصوص والحواف والـQueue والـEvals؛
- سلامة واجهات الإنسان وروابط المصادر الرسمية؛
- روابط التنقل في النصوص المجزأة؛
- سلامة حزم النسخ الموحدة ومسارات provenance؛
- تطابق Gold Eval cases مع expected outputs.

## ما الذي لا يختبره هذا الـWorkflow؟

لا يختبر توفر JORADP على الشبكة ولا صلاحية كل رابط PDF في اللحظة الحالية.

السبب: تعطل موقع خارجي أو DNS لا ينبغي أن يحول corpus صحيحا بنيويا إلى build فاشل.

اختبارات الوصول الفعلي إلى JORADP يجب أن تبقى في Workflow تكاملي منفصل مستقبلا، مع نتائج من نوع availability/integration ولا تختلط بالتحقق الحتمي للـcorpus.

## معنى PASS

نجاح الـWorkflow يعني أن commit المحدد مر بجميع الاختبارات الحتمية المعرفة حاليا في المستودع.

لا يعني PASS أن:

- كل transcription أصبحت `verified`؛
- كل حالة قانونية حُسمت؛
- كل dependency اكتُشفت؛
- JORADP متاح شبكيا؛
- الاستنتاجات القانونية غير المغطاة بالـValidator صحيحة تلقائيا.

الحالة القانونية ودرجة التحقق تبقيان محكومتين بالـprovenance وبحقول verification الخاصة بكل سجل.

## أول تشغيل مثبت

بتاريخ 2026-08-26 نجح التشغيل الأول للـCI على المستودع الفعلي، ثم نجح تشغيل ثان بعد تحديث Actions إلى الإصدارات الحديثة.

في التشغيل الأول سجل الـValidator:

```text
consolidated_segments: 8
consolidated_versions: 1
consolidation_map_rows: 45
discovery_queue: 28
eval_cases: 16
eval_expected: 16
graph_edges: 45
human_readmes: 17
metadata_records: 17
pdf_files: 0
segmented_files: 17
OK: no deterministic validation errors found.
```

كما مرت اختبارات JORADP Resolver الأربعة.

## Branch protection

في المرحلة الحالية لا يُفرض نجاح الـWorkflow كشرط حماية على `main` بعد. يظل CI مراقبة مستمرة مرئية.

بعد استقرار الـValidator واتساع corpus يمكن ترقية السياسة إلى:

`required status check before merge`

ويجب اتخاذ هذا القرار بصورة مستقلة بعد التأكد أن الـValidator لا يولد إخفاقات زائفة تعطل التطوير.
