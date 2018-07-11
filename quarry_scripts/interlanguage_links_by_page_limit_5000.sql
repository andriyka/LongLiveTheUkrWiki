use ukwiki_p;
select 
	ll.ll_from as page_id
	, count(*) as translations_count
from langlinks as ll
group by 
	ll.ll_from
   limit 5000