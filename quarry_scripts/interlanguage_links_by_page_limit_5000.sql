use ukwiki_p;
select 
	ll.ll_from as page_id
	, count(*) as translations_count
from langlinks as ll
join (select pp.page_id from page as pp limit 10000) as p
	on p.page_id = ll.ll_from
group by 
   ll.ll_from