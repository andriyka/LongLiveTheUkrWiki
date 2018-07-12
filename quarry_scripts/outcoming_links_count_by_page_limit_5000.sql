use ukwiki_p;
select 
	pl.pl_from as from_id
	, count(*) as links_count
from pagelinks as pl
join (select pp.page_id from page as pp limit 10000) as p
	on p.page_id = pl.pl_from
group by 
	pl.pl_from