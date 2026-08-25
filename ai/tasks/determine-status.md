# Task: determine-status

## الهدف

تحديد الحالة القانونية لنص في تاريخ معين بطريقة قابلة للتدقيق، دون افتراض أن النص القديم ملغى أو أن النص الأحدث ينسخه تلقائيا.

## Input

```yaml
text_id: null
as_of: "YYYY-MM-DD"
known_relations: []
official_sources: []
```

## Required process

1. حدد النص والنسخة والتاريخ المطلوب بدقة.
2. راجع أحكام النفاذ في النص نفسه.
3. ابحث عن نصوص لاحقة ذات أثر محتمل: تعديل، تتميم، إلغاء، تعليق، استبدال أو انتهاء محدد المدة.
4. تحقق من كل أثر في المصدر الرسمي.
5. افصل بين حالة النص ككل وحالة مواد بعينها.
6. إذا كانت الوقائع لا تكفي للحسم، استخدم `unknown` أو حالة مركبة موثقة بدل التخمين.
7. سجل `status_as_of` دائما.

## Output

```yaml
legal_status:
  text_id: null
  value: unknown
  status_as_of: null
  affected_articles: []
  evidence: []
  reasoning_summary: null
  verification_stage: machine_extracted
  unresolved_questions: []
```

## قواعد

- `confidence` لا يكفي وحده.
- وجود تعديل لا يعني إلغاء النص.
- وجود نص جديد في الموضوع نفسه لا يعني `replaced` بلا دليل.
- الإلغاء الجزئي يجب أن يحدد نطاقه قدر الإمكان.
- تاريخ النشر وتاريخ النفاذ قد يختلفان.
