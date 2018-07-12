use ukwiki_p;
select 
	pl.pl_from as from_id
	, count(*) as blue_links_count
from pagelinks as pl
join 
(select pp.page_title from page as pp limit 1)
as p
	on p.page_title = pl.pl_title
group by 
	pl.pl_from
