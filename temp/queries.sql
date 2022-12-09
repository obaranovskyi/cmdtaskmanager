select * from task;
select * from status;
select * from tag;
select * from task_tag;
select * from project;
select * from status_change_reason;

select t.id, t.value, tt.task_id, ta.title from task_tag as tt
join tag as t on t.id = tt.tag_id
join task as ta on ta.id = tt.task_id
where tt.task_id = 1;


select t.id, t.value, tk.id as task_id, tk.title as task_title
from tag as t
join task_tag as tt on tt.tag_id = t.id
join task as tk on tk.id = tt.task_id
where t.value = 'RealProject';

-- drop all tables
drop table status_change_reason;
drop table status;
drop table task_tag;
drop table tag;
drop table project;
drop table task;


-- Find add tasks that have tag with the given id
SELECT task.id AS task_id, 
       task.title AS task_title, 
       task.description AS task_description, 
       task.long_description AS task_long_description, 
       task.priority AS task_priority, 
       task.status_id AS task_status_id, 
       task.project_id AS task_project_id, 
       task.date_created AS task_date_created, 
       task.finish_date AS task_finish_date
FROM task 
JOIN task_tag ON task.id = task_tag.task_id 
JOIN tag ON tag.id = task_tag.tag_id
WHERE task_tag.tag_id = 1;
