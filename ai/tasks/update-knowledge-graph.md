# Task: update-knowledge-graph

## الهدف

تحديث شبكة العلاقات والفهارس من records موثقة دون إدخال استنتاجات جديدة غير موجودة في المصدر أو metadata المعتمدة.

## Input

```yaml
records: []
minimum_verification_stage: source_checked
```

## Required process

1. تحقق من أن كل record بلغ مرحلة التحقق المطلوبة.
2. أنشئ nodes للنصوص والمواد والجهات فقط وفق نموذج البيانات المعتمد.
3. أنشئ edges من العلاقات المصدرية المثبتة.
4. ولد العلاقات العكسية المشتقة آليا حيث يسمح ontology بذلك.
5. لا تحول topic similarity أو citation proximity إلى علاقة قانونية.
6. حافظ على provenance أو معرف العلاقة الأصلية في الحواف المشتقة.
7. اكشف التعارضات، التكرار، targets غير المحلولة، والحواف الدائرية غير المتوقعة.

## Output

```yaml
graph_update:
  nodes_added: []
  edges_added: []
  derived_edges_added: []
  unresolved_targets: []
  conflicts: []
  validation_errors: []
```

## قاعدة مهمة

Knowledge Graph ليس مكانا لاختراع الدلالة؛ هو تمثيل قابل للاستعلام لما ثبت في records والعلاقات الموثقة.