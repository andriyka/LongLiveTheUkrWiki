use ukwiki_p;
select 
	pl.pl_from as from_id
    , p.page_id as to_id
	, count(*) as links_count
from pagelinks as pl
join (select pp.page_id from page as pp limit 10000 ) as pin
	on pin.page_id = pl.pl_from
left join page p
	on p.page_title = pl.pl_title
group by 
	pl.pl_from
    , p.page_id
