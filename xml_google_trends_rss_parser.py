# Google Trends - trending searches XML/RSS parser
# Google Trends URL: https://trends.google.com/trends/trendingsearches/daily?geo=US&hl=en-US
# RSS format: https://trends.google.com/trends/trendingsearches/daily/rss?geo=US
# Just copy data from RSS format in xml_data variable and then run script to get Python list of trending searches

import xml.etree.ElementTree as ET
from html import unescape

# XML data (your original XML data with problematic characters)
xml_data = '''
<rss xmlns:atom="http://www.w3.org/2005/Atom" xmlns:ht="https://trends.google.com/trends/trendingsearches/daily" version="2.0">
<channel>
<title>Daily Search Trends</title>
<description>Recent searches</description>
<link>https://trends.google.com/trends/trendingsearches/daily?geo=US</link>
<atom:link href="https://trends.google.com/trends/trendingsearches/daily/rss?geo=US" rel="self" type="application/rss+xml"/>
<item>
<title>Travis Scott</title>
<ht:approx_traffic>20,000+</ht:approx_traffic>
<description/>
<link>https://trends.google.com/trends/trendingsearches/daily?geo=US#Travis%20Scott</link>
<pubDate>Thu, 20 Jun 2024 07:00:00 -0700</pubDate>
<ht:picture>https://t0.gstatic.com/images?q=tbn:ANd9GcTfcohHa8R0GP-teYvbsq-2fNI9RrvDpoGjB3I2hxLIElDGr4HTv62Zan6I3YMDhPRdjUTGA76Z</ht:picture>
<ht:picture_source>BBC News</ht:picture_source>
<ht:news_item>
<ht:news_item_title>Travis Scott arrested in Miami over intoxication and trespassing</ht:news_item_title>
<ht:news_item_snippet>The rapper is detained under his real name, Jacques Bermon Webster, according to custody records.</ht:news_item_snippet>
<ht:news_item_url>https://www.bbc.com/news/articles/cldd457vk3ro</ht:news_item_url>
<ht:news_item_source>BBC News</ht:news_item_source>
</ht:news_item>
<ht:news_item>
<ht:news_item_title>Rapper Travis Scott arrested on disorderly intoxication charge in ...</ht:news_item_title>
<ht:news_item_snippet>Rapper Travis Scott was arrested early Thursday on a disorderly intoxication charge after allegedly yelling at people on a yacht in Miami Beach, Florida,&nbsp;...</ht:news_item_snippet>
<ht:news_item_url>https://www.nbcnews.com/news/us-news/rapper-travis-scott-arrested-disorderly-intoxication-miami-dade-county-rcna158014</ht:news_item_url>
<ht:news_item_source>NBC News</ht:news_item_source>
</ht:news_item>
</item>
<item>
<title>Tyler, the Creator</title>
<ht:approx_traffic>20,000+</ht:approx_traffic>
<description/>
<link>https://trends.google.com/trends/trendingsearches/daily?geo=US#Tyler,%20the%20Creator</link>
<pubDate>Thu, 20 Jun 2024 09:00:00 -0700</pubDate>
<ht:picture>https://t1.gstatic.com/images?q=tbn:ANd9GcT5e4H7aN3VvWRzmwZadQ3nB4HAfEYAlMTYNDfBr2MHFiT1mxOCCZIzAkSI4eXxeJHAyIZ9w-aQ</ht:picture>
<ht:picture_source>Variety</ht:picture_source>
<ht:news_item>
<ht:news_item_title>Tyler the Creator Cancels Lollapalooza and Outside Lands ...</ht:news_item_title>
<ht:news_item_snippet>Tyler, the Creator pulled out of his headlining sets at Lollapalooza and Outside Lands. He is replaced by Megan Thee Stallion and Sabrina Carpenter.</ht:news_item_snippet>
<ht:news_item_url>https://variety.com/2024/music/news/tyler-the-creator-cancels-lollapalooza-outside-lands-1236043099/</ht:news_item_url>
<ht:news_item_source>Variety</ht:news_item_source>
</ht:news_item>
<ht:news_item>
<ht:news_item_title>Tyler, the Creator Drops Out of Lollapalooza, Outside Lands ...</ht:news_item_title>
<ht:news_item_snippet>Tyler, the Creator dropped out as headliner at Lollapalooza and Outside Lands. Megan Thee Stallion and Sabrina Carpenter will replace him.</ht:news_item_snippet>
<ht:news_item_url>https://www.rollingstone.com/music/music-news/tyler-the-creator-lollapalooza-outside-lands-megan-thee-stallion-sabrina-carpenter-1235043041/</ht:news_item_url>
<ht:news_item_source>Rolling Stone</ht:news_item_source>
</ht:news_item>
</item>
<item>
<title>Full moon</title>
<ht:approx_traffic>20,000+</ht:approx_traffic>
<description/>
<link>https://trends.google.com/trends/trendingsearches/daily?geo=US#Full%20moon</link>
<pubDate>Thu, 20 Jun 2024 07:00:00 -0700</pubDate>
<ht:picture>https://t0.gstatic.com/images?q=tbn:ANd9GcS_TnrGpXlvEPYYmuweJhFdh0r2-rEhyueAnbdkBS_ldo3i9DkEkEDg2hWuyNn8xR_cHkE3lzhJ</ht:picture>
<ht:picture_source>The Tennessean</ht:picture_source>
<ht:news_item>
<ht:news_item_title>When is the next full moon? We are in for a sweet treat for June</ht:news_item_title>
<ht:news_item_snippet>The summer solstice and the first official day of summer astronomically for 2024 is Thursday, June 20, which is when the Northern Hemisphere has the longest day&nbsp;...</ht:news_item_snippet>
<ht:news_item_url>https://www.tennessean.com/story/news/2024/06/20/june-2024-full-moon-strawberry-moon-meaning-tennessee-views/74134497007/</ht:news_item_url>
<ht:news_item_source>The Tennessean</ht:news_item_source>
</ht:news_item>
<ht:news_item>
<ht:news_item_title>The summer solstices&#39; impact on June&#39;s full strawberry moon</ht:news_item_title>
<ht:news_item_snippet>The summer solstice occurs in the northern hemisphere annually on June 20 or 21. It is when the sun is directly over the Tropic of Cancer and is located the&nbsp;...</ht:news_item_snippet>
<ht:news_item_url>https://spectrumlocalnews.com/nc/triad/weather/2024/06/20/the-summer-solstices--impact-on-june-s-full-strawberry-moon</ht:news_item_url>
<ht:news_item_source>Spectrum News</ht:news_item_source>
</ht:news_item>
</item>
<item>
<title>Summer solstice 2024</title>
<ht:approx_traffic>200,000+</ht:approx_traffic>
<description>summer solstice, first day of summer</description>
<link>https://trends.google.com/trends/trendingsearches/daily?geo=US#Summer%20solstice%202024</link>
<pubDate>Wed, 19 Jun 2024 20:00:00 -0700</pubDate>
<ht:picture>https://t2.gstatic.com/images?q=tbn:ANd9GcQy96bmtMhb6B2Ld2-ooy5Jl-nAX6sgY6xtkSvrsHR6A_DF9kjgvf7lkJjCn25RiYj22q7gBt6e</ht:picture>
<ht:picture_source>Aljazeera.com</ht:picture_source>
<ht:news_item>
<ht:news_item_title>Summer solstice 2024: Is it going to get even hotter now?</ht:news_item_title>
<ht:news_item_snippet>While Thursday marks the longest day of the year in Northern Hemisphere, it will not necessarily be the hottest.</ht:news_item_snippet>
<ht:news_item_url>https://www.aljazeera.com/news/2024/6/20/summer-solstice-2024-is-it-going-to-get-even-hotter-now</ht:news_item_url>
<ht:news_item_source>Aljazeera.com</ht:news_item_source>
</ht:news_item>
<ht:news_item>
<ht:news_item_title>Summer solstice 2024 marks the longest day in the Northern ...</ht:news_item_title>
<ht:news_item_snippet>The summer solstice, also known as the June solstice arrives June 20 at 4:51 p.m. EDT (2051 GMT), marking the longest day in the Northern Hemisphere.</ht:news_item_snippet>
<ht:news_item_url>https://www.space.com/summer-solstice-2024-longest-day-of-the-year</ht:news_item_url>
<ht:news_item_source>Space.com</ht:news_item_source>
</ht:news_item>
</item>
<item>
<title>NHL</title>
<ht:approx_traffic>200,000+</ht:approx_traffic>
<description/>
<link>https://trends.google.com/trends/trendingsearches/daily?geo=US#NHL</link>
<pubDate>Wed, 19 Jun 2024 02:00:00 -0700</pubDate>
<ht:picture>https://t1.gstatic.com/images?q=tbn:ANd9GcRsSY3A2Hvwv8WySmKwhV7CgMWZV0mfrPHp8k8PU9QZpKXN5HQV4mwtXwla8u2gtksq31B5vyqS</ht:picture>
<ht:picture_source>NHL.com</ht:picture_source>
<ht:news_item>
<ht:news_item_title>Masse&#39;s production when it counts turning heads heading into 2024 ...</ht:news_item_title>
<ht:news_item_snippet>Maxim Masse of Chicoutimi of the Quebec Maritimes Junior Hockey League seems to have a knack for coming up big in the clutch. The most memorable of his 13 game-&nbsp;...</ht:news_item_snippet>
<ht:news_item_url>https://www.nhl.com/news/maxim-masse-clutch-play-impressing-ahead-2024-nhl-draft</ht:news_item_url>
<ht:news_item_source>NHL.com</ht:news_item_source>
</ht:news_item>
</item>
<item>
<title>Kendrick Lamar</title>
<ht:approx_traffic>200,000+</ht:approx_traffic>
<description>kendrick lamar concert, Drake</description>
<link>https://trends.google.com/trends/trendingsearches/daily?geo=US#Kendrick%20Lamar</link>
<pubDate>Wed, 19 Jun 2024 17:00:00 -0700</pubDate>
<ht:picture>https://t1.gstatic.com/images?q=tbn:ANd9GcQgIW74f3-a_2Qsmp0QCUOtUt39ShWCuaAV-ROKMyS-YxSAqe6XVEn9pqKXKVJmZMIu0pkonc-g</ht:picture>
<ht:picture_source>The Associated Press</ht:picture_source>
<ht:news_item>
<ht:news_item_title>After Drake battle, Kendrick Lamar turns victory lap concert into LA ...</ht:news_item_title>
<ht:news_item_snippet>Kendrick Lamar turned his Juneteenth “Pop Out” concert at the Forum into a cathartic livestreamed celebration of Los Angeles unity.</ht:news_item_snippet>
<ht:news_item_url>https://apnews.com/article/kendrick-lamar-pop-out-concert-977958e25837f56a73dd2379db43f916</ht:news_item_url>
<ht:news_item_source>The Associated Press</ht:news_item_source>
</ht:news_item>
<ht:news_item>
<ht:news_item_title>Here&#39;s Everything That Happened at Kendrick Lamar&#39;s Juneteenth ...</ht:news_item_title>
<ht:news_item_snippet>Dozens of West Coast rappers joined Lamar on stage at The Forum following his Drake beef.</ht:news_item_snippet>
<ht:news_item_url>https://www.rollingstone.com/music/music-live-reviews/kendrick-lamars-juneteenth-concert-the-pop-out-1235042890/</ht:news_item_url>
<ht:news_item_source>Rolling Stone</ht:news_item_source>
</ht:news_item>
</item>
<item>
<title>Mystics vs Fever</title>
<ht:approx_traffic>100,000+</ht:approx_traffic>
<description>Indiana Fever</description>
<link>https://trends.google.com/trends/trendingsearches/daily?geo=US#Mystics%20vs%20Fever</link>
<pubDate>Wed, 19 Jun 2024 17:00:00 -0700</pubDate>
<ht:picture>https://t2.gstatic.com/images?q=tbn:ANd9GcT6zKWGEkaR7GFNILC55ZMsythH5t1fE_y-PCx91G1mvXdxJPD1xA6UJ_3rsgcwQqKGI1E0DCOE</ht:picture>
<ht:picture_source>The Indianapolis Star</ht:picture_source>
<ht:news_item>
<ht:news_item_title>FINAL: Indiana Fever take down Washington Mystics, Caitlin Clark ...</ht:news_item_title>
<ht:news_item_snippet>The Indiana Fever will look to extend their winning streak to three games as they take on the Washington Mystics.</ht:news_item_snippet>
<ht:news_item_url>https://www.indystar.com/story/sports/basketball/wnba/fever/2024/06/19/indiana-fever-washington-mystics-live-updates-caitlin-clark-highlights-stats-score-aliyah-boston/74142861007/</ht:news_item_url>
<ht:news_item_source>The Indianapolis Star</ht:news_item_source>
</ht:news_item>
<ht:news_item>
<ht:news_item_title>Fever vs. Mystics odds, time, spread: 2024 WNBA picks, Caitlin ...</ht:news_item_title>
<ht:news_item_snippet>SportsLine&#39;s women&#39;s basketball expert Calvin Wetzel has revealed his top picks for Caitlin Clark and the Indiana Fever vs. the Washington Mystics on&nbsp;...</ht:news_item_snippet>
<ht:news_item_url>https://www.cbssports.com/wnba/news/fever-vs-mystics-odds-time-spread-2024-wnba-picks-caitlin-clark-predictions-for-june-19-by-proven-expert/</ht:news_item_url>
<ht:news_item_source>CBSSports.com</ht:news_item_source>
</ht:news_item>
</item>
<item>
<title>Robert Morris</title>
<ht:approx_traffic>100,000+</ht:approx_traffic>
<description>gateway church, pastor Robert Morris</description>
<link>https://trends.google.com/trends/trendingsearches/daily?geo=US#Robert%20Morris</link>
<pubDate>Wed, 19 Jun 2024 06:00:00 -0700</pubDate>
<ht:picture>https://t3.gstatic.com/images?q=tbn:ANd9GcTo2-s7ayJxK1BA8KpBlIW18egk1ibyXYDl5hTPguKgQV5HJG4DFTpUncaBgWMJjIaWJXM0hd-N</ht:picture>
<ht:picture_source>CNN</ht:picture_source>
<ht:news_item>
<ht:news_item_title>Texas megachurch accepts senior pastor&#39;s resignation after ...</ht:news_item_title>
<ht:news_item_snippet>A Dallas-area megachurch accepted the resignation of senior pastor Robert Morris on Tuesday after allegations of a past inappropriate relationship with a&nbsp;...</ht:news_item_snippet>
<ht:news_item_url>https://www.cnn.com/2024/06/18/us/robert-morris-gateway-church-sexual-abuse-allegations-resignation/index.html</ht:news_item_url>
<ht:news_item_source>CNN</ht:news_item_source>
</ht:news_item>
<ht:news_item>
<ht:news_item_title>Texas megachurch pastor resigns amid allegations he sexually ...</ht:news_item_title>
<ht:news_item_snippet>A pastor at a Texas megachurch resigned Tuesday after a woman accused him of sexually abusing her several times between 1982 and 1987, when she was a minor.</ht:news_item_snippet>
<ht:news_item_url>https://www.washingtonpost.com/nation/2024/06/19/texas-gateway-church-pastor-abuse/</ht:news_item_url>
<ht:news_item_source>The Washington Post</ht:news_item_source>
</ht:news_item>
</item>
<item>
<title>Germany vs Hungary</title>
<ht:approx_traffic>100,000+</ht:approx_traffic>
<description/>
<link>https://trends.google.com/trends/trendingsearches/daily?geo=US#Germany%20vs%20Hungary</link>
<pubDate>Wed, 19 Jun 2024 10:00:00 -0700</pubDate>
<ht:picture>https://t0.gstatic.com/images?q=tbn:ANd9GcTtv4xd4EJUWg5c2DMpV-atyxxS7uIaho3iywFJu3GrDuzznzKzAcL6UO_ot4M6ARX1OXoT3NlV</ht:picture>
<ht:picture_source>The Athletic</ht:picture_source>
<ht:news_item>
<ht:news_item_title>Germany vs Hungary live updates: Musiala and Gundogan goals ...</ht:news_item_title>
<ht:news_item_snippet>Follow live reaction to Germany&#39;s 2-0 victory over Hungary at the European Championship.</ht:news_item_snippet>
<ht:news_item_url>https://www.nytimes.com/athletic/live-blogs/germany-hungary-live-updates-euro-2024-score-result/U5Y15Su6ZNHH/</ht:news_item_url>
<ht:news_item_source>The Athletic</ht:news_item_source>
</ht:news_item>
<ht:news_item>
<ht:news_item_title>Germany vs. Hungary highlights: Germany wins 2-0, clinches spot in ...</ht:news_item_title>
<ht:news_item_snippet>Euro 2024 continued on Wednesday, as Germany beat Hungary in Group A, 2-0. Here are the top moments from the match!</ht:news_item_snippet>
<ht:news_item_url>https://www.foxsports.com/live-blog/soccer/germany-vs-hungary-live-updates-score-top-moments-from-euro-2024</ht:news_item_url>
<ht:news_item_source>FOXSports.com</ht:news_item_source>
</ht:news_item>
</item>
<item>
<title>Tennessee baseball</title>
<ht:approx_traffic>100,000+</ht:approx_traffic>
<description>Florida baseball</description>
<link>https://trends.google.com/trends/trendingsearches/daily?geo=US#Tennessee%20baseball</link>
<pubDate>Wed, 19 Jun 2024 14:00:00 -0700</pubDate>
<ht:picture>https://t0.gstatic.com/images?q=tbn:ANd9GcQZpgDk6tGHOkLt3sbrQGFNICmP1MgGhwaHTn3Itp2Llzz_wzrfZRasYtSQIhc6oII0qd635UPF</ht:picture>
<ht:picture_source>Tallahassee.com</ht:picture_source>
<ht:news_item>
<ht:news_item_title>Florida State baseball&#39;s bounce back season ends in College World ...</ht:news_item_title>
<ht:news_item_snippet>Follow live score updates as Florida State baseball is back in the College World Series semifinals for the first time in 12 years, facing Tennessee.</ht:news_item_snippet>
<ht:news_item_url>https://www.tallahassee.com/story/sports/college/fsu/baseball/2024/06/19/score-updates-from-fsu-baseballs-college-world-series-rematch-against-tennessee/74148467007/</ht:news_item_url>
<ht:news_item_source>Tallahassee.com</ht:news_item_source>
</ht:news_item>
<ht:news_item>
<ht:news_item_title>Inside two plays that showed why Tennessee baseball will play for ...</ht:news_item_title>
<ht:news_item_snippet>Tennessee baseball made two third-inning plays that showed the maturity that coach Tony Vitello has raved about. It&#39;s why UT is in the CWS final.</ht:news_item_snippet>
<ht:news_item_url>https://www.knoxnews.com/story/sports/college/university-of-tennessee/other-sports/2024/06/19/tennessee-baseball-florida-state-college-world-series-final-tony-vitello/74042607007/</ht:news_item_url>
<ht:news_item_source>Knoxville News Sentinel</ht:news_item_source>
</ht:news_item>
</item>
<item>
<title>Stonehenge</title>
<ht:approx_traffic>50,000+</ht:approx_traffic>
<description>stonehenge vandalism</description>
<link>https://trends.google.com/trends/trendingsearches/daily?geo=US#Stonehenge</link>
<pubDate>Wed, 19 Jun 2024 13:00:00 -0700</pubDate>
<ht:picture>https://t2.gstatic.com/images?q=tbn:ANd9GcRomxhPaOD0AYEqA7VK7dD75an-HdwMrzgKcNQGB6hyVXimHT0hV5rn4HKgUlE_RbHSXQq5qHFq</ht:picture>
<ht:picture_source>The Associated Press</ht:picture_source>
<ht:news_item>
<ht:news_item_title>Stonehenge not visibly damaged by protest paint. It&#39;s clean and ...</ht:news_item_title>
<ht:news_item_snippet>Stonehenge monuments that have stood for thousands of years appear unscathed after climate protesters were arrested for spraying orange paint on them.</ht:news_item_snippet>
<ht:news_item_url>https://apnews.com/article/stonehenge-vandalism-paint-climate-protest-summer-solstice-f93506fdd75d9b5b8be1725f11ad8b33</ht:news_item_url>
<ht:news_item_source>The Associated Press</ht:news_item_source>
</ht:news_item>
<ht:news_item>
<ht:news_item_title>Stonehenge Sprayed With Orange Paint One Day Before Solstice</ht:news_item_title>
<ht:news_item_snippet>Stonehenge was been sprayed with orange paint by climate activists on Jun. 19 demanding action on fossil fuels just one day before summer solstice.</ht:news_item_snippet>
<ht:news_item_url>https://www.forbes.com/sites/jamiecartereurope/2024/06/19/stonehenge-sprayed-with-orange-paint-on-the-day-before-summer-solstice/</ht:news_item_url>
<ht:news_item_source>Forbes</ht:news_item_source>
</ht:news_item>
</item>
<item>
<title>Croatia vs Albania</title>
<ht:approx_traffic>50,000+</ht:approx_traffic>
<description/>
<link>https://trends.google.com/trends/trendingsearches/daily?geo=US#Croatia%20vs%20Albania</link>
<pubDate>Wed, 19 Jun 2024 07:00:00 -0700</pubDate>
<ht:picture>https://t2.gstatic.com/images?q=tbn:ANd9GcTZmiYmWjomrP7Xj9HHXtmQZ7JHOfFZzQ8YPWaxESrhPkBqP1qcgxq5mm2kGxj2JqVHN6gnqBbQ</ht:picture>
<ht:picture_source>Goal.com</ht:picture_source>
<ht:news_item>
<ht:news_item_title>Croatia vs Albania Predictions and Betting Tips: Sylvinho&#39;s Side Can ...</ht:news_item_title>
<ht:news_item_snippet>Find out about our soccer betting expert&#39;s Croatia vs Albania betting tips and predictions for Wednesday&#39;s Euro 2024 Group B clash in Hamburg.</ht:news_item_snippet>
<ht:news_item_url>https://www.goal.com/en-us/betting/croatia-vs-albania-predictions-tips-06-19/blt4b58400d45c6693b</ht:news_item_url>
<ht:news_item_source>Goal.com</ht:news_item_source>
</ht:news_item>
<ht:news_item>
<ht:news_item_title>Croatia vs Albania live updates: Late Klaus Gjasula goal secures ...</ht:news_item_title>
<ht:news_item_snippet>What a start to day six at Euro 2024! I&#39;m sure you&#39;ll be glad to hear that there are two more matches coming your way today, and The Athletic is covering&nbsp;...</ht:news_item_snippet>
<ht:news_item_url>https://www.nytimes.com/athletic/live-blogs/croatia-albania-live-updates-euro-2024-score-result/BjlJDTU1qes9/</ht:news_item_url>
<ht:news_item_source>The Athletic</ht:news_item_source>
</ht:news_item>
</item>
<item>
<title>CDK cyberattack</title>
<ht:approx_traffic>50,000+</ht:approx_traffic>
<description/>
<link>https://trends.google.com/trends/trendingsearches/daily?geo=US#CDK%20cyberattack</link>
<pubDate>Wed, 19 Jun 2024 13:00:00 -0700</pubDate>
<ht:picture>https://t0.gstatic.com/images?q=tbn:ANd9GcRVaIYA2N7jNFpzOMPxlUj6WAJgZRIimo0R7-ixA7OS3ubk3yPr0DGpIqy6-wvX_XZTcVgqzXTp</ht:picture>
<ht:picture_source>USA TODAY</ht:picture_source>
<ht:news_item>
<ht:news_item_title>CDK Global shuts down car dealership software after cyberattack</ht:news_item_title>
<ht:news_item_snippet>A leading software provider to U.S. car dealerships has shut down most of its systems “out of an abundance of caution&quot; after a cyber attack.</ht:news_item_snippet>
<ht:news_item_url>https://www.usatoday.com/story/money/cars/2024/06/19/cdk-cyber-attack-hits-automotive-dealers/74150427007/</ht:news_item_url>
<ht:news_item_source>USA TODAY</ht:news_item_source>
</ht:news_item>
<ht:news_item>
<ht:news_item_title>CDK Global cyberattack disrupts operations at 15000 dealerships</ht:news_item_title>
<ht:news_item_snippet>CDK Global, a major software provider to auto dealerships in the U.S., has been hacked, forcing the company to shut down temporarily.</ht:news_item_snippet>
<ht:news_item_url>https://www.cbtnews.com/cdk-global-cyberattack-disrupts-operations-at-15000-dealerships/</ht:news_item_url>
<ht:news_item_source>http://cbtnews.com/</ht:news_item_source>
</ht:news_item>
</item>
<item>
<title>Ten Commandments</title>
<ht:approx_traffic>50,000+</ht:approx_traffic>
<description>louisiana ten commandments</description>
<link>https://trends.google.com/trends/trendingsearches/daily?geo=US#Ten%20Commandments</link>
<pubDate>Wed, 19 Jun 2024 19:00:00 -0700</pubDate>
<ht:picture>https://t2.gstatic.com/images?q=tbn:ANd9GcRdYDq2BJ_Qtdje1BUPtD_m0fap4o0NWcw6IBN7G_7HPDJcljkV-ydagJrqxuKtnBHDme5xy5lN</ht:picture>
<ht:picture_source>BBC News</ht:picture_source>
<ht:news_item>
<ht:news_item_title>Louisiana orders Ten Commandments poster in every classroom</ht:news_item_title>
<ht:news_item_snippet>A historic new law requires a poster in every public-school classroom - but campaigners will challenge it.</ht:news_item_snippet>
<ht:news_item_url>https://www.bbc.com/news/articles/cp66xdxj0l3o</ht:news_item_url>
<ht:news_item_source>BBC News</ht:news_item_source>
</ht:news_item>
<ht:news_item>
<ht:news_item_title>Louisiana will face lawsuit over Ten Commandments school ...</ht:news_item_title>
<ht:news_item_snippet>Four civil liberties groups will sue the state of Louisiana after Gov. Jeff Landry signed a law that calls for the Ten Commandments to be displayed in&nbsp;...</ht:news_item_snippet>
<ht:news_item_url>https://lailluminator.com/2024/06/19/ten-commandments-4/</ht:news_item_url>
<ht:news_item_source>Louisiana Illuminator</ht:news_item_source>
</ht:news_item>
</item>
<item>
<title>Juneteenth flag</title>
<ht:approx_traffic>50,000+</ht:approx_traffic>
<description/>
<link>https://trends.google.com/trends/trendingsearches/daily?geo=US#Juneteenth%20flag</link>
<pubDate>Wed, 19 Jun 2024 06:00:00 -0700</pubDate>
<ht:picture>https://t0.gstatic.com/images?q=tbn:ANd9GcTbSuS-LjBA5f_EF3XP2e3o_OsZbLHAVCdxXLv9vDmXE0iKaWjuKtkuVXH1N97gqqzHg3yIqXOp</ht:picture>
<ht:picture_source>State House News Service</ht:picture_source>
<ht:news_item>
<ht:news_item_title>Juneteenth flag</ht:news_item_title>
<ht:news_item_snippet>A flag honoring Juneteenth is raised outside the State House on Wednesday, June 19, 2024.</ht:news_item_snippet>
<ht:news_item_url>https://www.statehousenews.com/juneteenth-flag/image_1eccb77e-2e60-11ef-a25c-ab6bfb33d9f9.html</ht:news_item_url>
<ht:news_item_source>State House News Service</ht:news_item_source>
</ht:news_item>
<ht:news_item>
<ht:news_item_title>Bridgewater turns out for Juneteenth flag raising</ht:news_item_title>
<ht:news_item_snippet>Hugh Holmes Jr., originally of Bridgewater and now of Fall River, listens to the speakers from Bridgewater-Raynham Regional High School during the&nbsp;...</ht:news_item_snippet>
<ht:news_item_url>https://www.enterprisenews.com/picture-gallery/news/local/2024/06/19/bridgewater-ma-juneteenth-flag-raising-town-hall/74131880007/</ht:news_item_url>
<ht:news_item_source>Enterprise News</ht:news_item_source>
</ht:news_item>
</item>
<item>
<title>Katie Ledecky</title>
<ht:approx_traffic>50,000+</ht:approx_traffic>
<description/>
<link>https://trends.google.com/trends/trendingsearches/daily?geo=US#Katie%20Ledecky</link>
<pubDate>Wed, 19 Jun 2024 21:00:00 -0700</pubDate>
<ht:picture>https://t1.gstatic.com/images?q=tbn:ANd9GcQ-12HRhLPrM7YDd1sy6SwXXGVFUB8CojWW3n_CV3stdJszJYFqTMwqHl6TSPpHzgfWBxOjD7Yy</ht:picture>
<ht:picture_source>USA TODAY</ht:picture_source>
<ht:news_item>
<ht:news_item_title>Katie Ledecky dominates 1500 at Olympic trials, exactly as expected</ht:news_item_title>
<ht:news_item_snippet>Ledecky, the greatest female swimmer in history, won her third consecutive event Wednesday night, the longest race in the pool, the 1500 freestyle.</ht:news_item_snippet>
<ht:news_item_url>https://www.usatoday.com/story/sports/olympics/2024/06/19/katie-ledecky-olympic-trials-1500-win/74152774007/</ht:news_item_url>
<ht:news_item_source>USA TODAY</ht:news_item_source>
</ht:news_item>
<ht:news_item>
<ht:news_item_title>U.S. Olympic Trials, Day 5 Finals: Katie Ledecky to Defend 1500 ...</ht:news_item_title>
<ht:news_item_snippet>Katie Ledecky dominated the 1500 freestyle to secure another event at the Paris Olympics while Katie Grimes also qualified.</ht:news_item_snippet>
<ht:news_item_url>https://www.swimmingworldmagazine.com/news/u-s-olympic-trials-day-5-finals-katie-ledecky-to-defend-1500-free-title-katie-grimes-adds-another-event-in-paris/</ht:news_item_url>
<ht:news_item_source>Swimming World Magazine</ht:news_item_source>
</ht:news_item>
</item>
<item>
<title>Monty Williams</title>
<ht:approx_traffic>50,000+</ht:approx_traffic>
<description/>
<link>https://trends.google.com/trends/trendingsearches/daily?geo=US#Monty%20Williams</link>
<pubDate>Wed, 19 Jun 2024 09:00:00 -0700</pubDate>
<ht:picture>https://t1.gstatic.com/images?q=tbn:ANd9GcTRCgi6cMjDO1JBoAR0iglrpuP2q1nHXWpRSFvai3TU4apeO5QNEqB3xyWrOJzmxkiwebB4jOX2</ht:picture>
<ht:picture_source>NBA.com</ht:picture_source>
<ht:news_item>
<ht:news_item_title>Pistons dismiss coach Monty Williams after 1 season | NBA.com</ht:news_item_title>
<ht:news_item_snippet>The Pistons are moving on from coach Monty Williams, who went 14-68 in his lone season with Detroit in 2023-24.</ht:news_item_snippet>
<ht:news_item_url>https://www.nba.com/news/pistons-dismiss-coach-monty-williams</ht:news_item_url>
<ht:news_item_source>NBA.com</ht:news_item_source>
</ht:news_item>
<ht:news_item>
<ht:news_item_title>Monty Williams&#39; firing will hopefully signify a legitimate step forward ...</ht:news_item_title>
<ht:news_item_snippet>With Trajan Langdon now running things in Detroit, the franchise needs one voice and one vision as it aspires for relevance.</ht:news_item_snippet>
<ht:news_item_url>https://sports.yahoo.com/monty-williams-firing-will-hopefully-signify-a-legitimate-step-forward-for-the-pistons-190153380.html</ht:news_item_url>
<ht:news_item_source>Yahoo Sports</ht:news_item_source>
</ht:news_item>
</item>
<item>
<title>Scotland vs Switzerland</title>
<ht:approx_traffic>50,000+</ht:approx_traffic>
<description/>
<link>https://trends.google.com/trends/trendingsearches/daily?geo=US#Scotland%20vs%20Switzerland</link>
<pubDate>Wed, 19 Jun 2024 13:00:00 -0700</pubDate>
<ht:picture>https://t2.gstatic.com/images?q=tbn:ANd9GcQMGGG_aAQBPu9FSWhjw2brL_AVW8IXyk6uxQoiuMNjUAD200OT-2_kbpLxaHbd07O6KWy4DKJa</ht:picture>
<ht:picture_source>The Athletic</ht:picture_source>
<ht:news_item>
<ht:news_item_title>Scotland vs Switzerland live updates: 1-1 draw keeps Scots&#39; Euro ...</ht:news_item_title>
<ht:news_item_snippet>Follow live reaction to Scotland&#39;s 1-1 draw with Switzerland at the European Championship.</ht:news_item_snippet>
<ht:news_item_url>https://www.nytimes.com/athletic/live-blogs/scotland-switzerland-live-updates-euro-2024-score-result/2iQeVTXu2wBD/</ht:news_item_url>
<ht:news_item_source>The Athletic</ht:news_item_source>
</ht:news_item>
<ht:news_item>
<ht:news_item_title>Scotland vs Switzerland Predictions and Betting Tips: Scots ...</ht:news_item_title>
<ht:news_item_snippet>Find out about our soccer betting expert&#39;s Scotland vs Switzerland predictions and betting tips ahead of their Euro 2024 clash at the RheinEnergieStadion,&nbsp;...</ht:news_item_snippet>
<ht:news_item_url>https://www.goal.com/en-us/betting/scotland-vs-switzerland-predictions-tips-06-19/blt2766a4b38e68391e</ht:news_item_url>
<ht:news_item_source>Goal.com</ht:news_item_source>
</ht:news_item>
</item>
<item>
<title>Tropical Storm Alberto</title>
<ht:approx_traffic>20,000+</ht:approx_traffic>
<description/>
<link>https://trends.google.com/trends/trendingsearches/daily?geo=US#Tropical%20Storm%20Alberto</link>
<pubDate>Wed, 19 Jun 2024 14:00:00 -0700</pubDate>
<ht:picture>https://t2.gstatic.com/images?q=tbn:ANd9GcRapIvou_VfRLT-LIVQq1enTUouRoaienLq4QE42BaVlhercQ63kYNElKLfVtdthE8IN0pQbpi1</ht:picture>
<ht:picture_source>Lone Star Live</ht:picture_source>
<ht:news_item>
<ht:news_item_title>Tropical Storm Alberto brings flooding, tornado warnings to Texas</ht:news_item_title>
<ht:news_item_snippet>By early Thursday, Alberto is expected to make landfall in eastern Mexico.</ht:news_item_snippet>
<ht:news_item_url>https://www.lonestarlive.com/weather/2024/06/tropical-storm-alberto-brings-flooding-tornado-warnings-to-texas.html</ht:news_item_url>
<ht:news_item_source>Lone Star Live</ht:news_item_source>
</ht:news_item>
<ht:news_item>
<ht:news_item_title>Tropical Storm Alberto turns deadly in Mexico as storm lashes Texas ...</ht:news_item_title>
<ht:news_item_snippet>Tropical Storm Alberto made landfall in northeastern Mexico early Thursday morning, leaving at least three people dead as impacts from the storm reached&nbsp;...</ht:news_item_snippet>
<ht:news_item_url>https://www.foxweather.com/weather-news/tracking-alberto-landfall-2024</ht:news_item_url>
<ht:news_item_source>FOX Weather</ht:news_item_source>
</ht:news_item>
</item>
<item>
<title>Ryan Garcia</title>
<ht:approx_traffic>20,000+</ht:approx_traffic>
<description/>
<link>https://trends.google.com/trends/trendingsearches/daily?geo=US#Ryan%20Garcia</link>
<pubDate>Wed, 19 Jun 2024 20:00:00 -0700</pubDate>
<ht:picture>https://t2.gstatic.com/images?q=tbn:ANd9GcTP4kK3MSO8C_KCQ0VJ7HRFyCQvzBnhE7VEIzeUCjrb3ElOWcshDgndSB7UlWxdT5alvS3yh4zy</ht:picture>
<ht:picture_source>New York Post</ht:picture_source>
<ht:news_item>
<ht:news_item_title>Ryan Garcia claims he&#39;s &#39;officially retired&#39; from boxing just over a ...</ht:news_item_title>
<ht:news_item_snippet>Boxer Ryan Garcia said he is now “officially retired” from boxing in a series of social media posts on Wednesday night amid some controversies he&#39;s been at&nbsp;...</ht:news_item_snippet>
<ht:news_item_url>https://nypost.com/2024/06/20/sports/ryan-garcia-claims-hes-officially-retired-from-boxing/</ht:news_item_url>
<ht:news_item_source>New York Post</ht:news_item_source>
</ht:news_item>
<ht:news_item>
<ht:news_item_title>Ryan Garcia says he&#39;s &#39;officially retired&#39; in string of posts lamenting ...</ht:news_item_title>
<ht:news_item_snippet>Less than two months after Ryan Garcia stunned the boxing world by defeating WBC super lightweight champ Devin Haney via majority decision,&nbsp;...</ht:news_item_snippet>
<ht:news_item_url>https://www.nytimes.com/athletic/5577337/2024/06/19/ryan-garcia-retirement-posts/</ht:news_item_url>
<ht:news_item_source>The Athletic</ht:news_item_source>
</ht:news_item>
</item>
</channel>
</rss>
'''


# Define a function to preprocess the XML data
def preprocess_xml_data(xml_data):
    # Replace problematic characters with entities
    xml_data.replace('&nbsp;', '&#160;')
    # Add more replacements as needed for other problematic characters
    # Decode HTML entities using unescape from html module
    return unescape(xml_data)


# Preprocess the XML data
preprocessed_xml_data = preprocess_xml_data(xml_data)

# Empty list
end_result = []

# Parse the preprocessed XML data
try:
    root = ET.fromstring(preprocessed_xml_data)
    # Process the XML tree here
    # For example:
    items = root.findall('.//item')
    for item in items:
        title = item.find('title').text
        # print(title)
        end_result.append(title)
    print(end_result)

except ET.ParseError as e:
    print(f"Error parsing XML: {e}")
