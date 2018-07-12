use ukwiki_p;
select 
	r.rev_page as page_id
    , min(r.rev_timestamp) as first_edit
from revision as r
group by 
	r.rev_page
limit 5000
