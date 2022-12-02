select * from task;
select * from status;
select * from tag;
select * from task_tag;

select t.id, t.value, tt.task_id, ta.title from task_tag as tt
join tag as t on t.id = tt.tag_id
join task as ta on ta.id = tt.task_id
where tt.task_id = 1;

select t.id, t.value, tk.id as task_id, tk.title as task_title
from tag as t
join task_tag as tt on tt.tag_id = t.id
join task as tk on tk.id = tt.task_id
where t.value = 'RealProject';
