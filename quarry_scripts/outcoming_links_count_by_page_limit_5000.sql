use ukwiki_p;
select 
	pl.pl_from as from_id
	, count(*) as links_count
from pagelinks as pl
group by 
	pl.pl_from
limit 5000