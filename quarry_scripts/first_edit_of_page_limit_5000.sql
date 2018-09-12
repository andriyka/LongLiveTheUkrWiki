use ukwiki_p;
select 
	r.rev_page as page_id
    , min(r.rev_timestamp) as first_edit
from revision as r
join (select pp.page_id from page as pp limit 10000) as p
	on p.page_id = r.rev_page
group by 
	r.rev_page
