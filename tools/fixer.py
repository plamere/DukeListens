import os
import sys

bm = """<!-- bookmarks -->

<div class="links sidebar-sect">
<div class="sidebar-sect-title">
<h2>Bookmarks</h2>
</div>
<div class="sidebar-sect-content">
<ul class="rFolder">
                    <li class="rFolderItem">
                                <a href="http://www.mediaor.com/" title="Aggregation of music blogs" class="rBookmark0">Me*dia*or</a>
                </li>
            <li class="rFolderItem">
                                <a href="http://mobblog.cs.ucl.ac.uk/" title="Research: Trust, Reputation, Recommendations and Mobility" class="rBookmark0">MobBlog</a>
                </li>
            <li class="rFolderItem">
                                <a href="offices_of_music_2_013.html" title="Photos of Music 2.0 Offices" class="rBookmark0">Offices</a>
                </li>
            <li class="rFolderItem">
                                <a href="http://research.sun.com/projects/dashboard.php?id=153" title="The search inside the music project page" class="rBookmark0">SITM</a>
                </li>
            <li class="rFolderItem">
                                <a href="https://savetherobot.wordpress.com/" title="Chris Dahlen's work blog" class="rBookmark0">Save the robot</a>
                </li>
            <li class="rFolderItem">
                                <a href="http://blogs.sun.com/searchguy/" title="" class="rBookmark0">Search Guy</a>
                </li>
            <li class="rFolderItem">
                                <a href="http://thetasteblog.com/" title="An aggregation of recommender blogs" class="rBookmark0">The Taste Blog</a>
                </li>
            <li class="rFolderItem">
                                <a href="http://musicmachinery.com/feed/"><img class="smrssbadge" src="support_files/smrssbadge.gif" alt="URL of site''s RSS feed"></a>
                        <a href="http://musicmachinery.com/" title="a blog about music technology" class="rBookmark10">Music Machinery</a>
                </li>
                    </ul>
</div>
</div>"""

feeds = """<!-- feeds not available in this archive, sorry -->
<div class="categories sidebar-sect">
   <div class="sidebar-sect-title">
   <h2>Categories</h2>
   <i>(Original blog had several other categories)</i>
   </div>
   <div class="sidebar-sect-content">
       <ul class="rCategory">
           <li><a href="category-freakomendations-page0.html">freakomendations</a></li>
       </ul>
   </div>
</div>
<!-- weblog menu not available in this archive, sorry -->
<!-- search not available in this archive, sorry -->
</form>
<script type="text/javascript">prepareSearchForm();</script>
</div>
</div>"""

recent = """<!-- recent entries -->

<div class="recent sidebar-sect default-expanded">
<div class="sidebar-sect-title">
<h2>Up to 10 Recent Entries</h2>
</div>
<div class="sidebar-sect-content">
  <ul>
      <li><a href="DukeListens/last_post.html">Last Post</a></li>
      <li><a href="DukeListens/the_best_job_in_the.html">The best job in the world</a></li>
      <li><a href="DukeListens/music_gone_viral.html">Music gone viral?</a></li>
      <li><a href="DukeListens/music_recommendation_and_the_long.html">Music Recommendation and the Long Tail</a></li>
      <li><a href="DukeListens/sxsw_artist_catalog_updated.html">SXSW Artist Catalog updated</a></li>
      <li><a href="DukeListens/most_overused_animals_of_indie.html">Most overused animals of indie rock?</a></li>
      <li><a href="DukeListens/blip_fm_api.html">Blip.fm API</a></li>
      <li><a href="DukeListens/new_release_of_sphinx_4.html">New release of Sphinx-4</a></li>
      <li><a href="DukeListens/styling_the_sxsw_artist_catalog.html">Styling the SXSW Artist Catalog</a></li>
      <li><a href="DukeListens/getting_the_most_space_on.html">Getting the most space on the marquee</a></li>
    </ul>
</div>
</div>"""

recent2= """<!-- recent entries -->

<div class="recent sidebar-sect default-expanded">
<div class="sidebar-sect-title">
<h2>Up to 10 Recent Entries</h2>
</div>
<div class="sidebar-sect-content">
  <ul>
      <li><a href="last_post.html">Last Post</a></li>
      <li><a href="the_best_job_in_the.html">The best job in the world</a></li>
      <li><a href="music_gone_viral.html">Music gone viral?</a></li>
      <li><a href="music_recommendation_and_the_long.html">Music Recommendation and the Long Tail</a></li>
      <li><a href="sxsw_artist_catalog_updated.html">SXSW Artist Catalog updated</a></li>
      <li><a href="most_overused_animals_of_indie.html">Most overused animals of indie rock?</a></li>
      <li><a href="blip_fm_api.html">Blip.fm API</a></li>
      <li><a href="new_release_of_sphinx_4.html">New release of Sphinx-4</a></li>
      <li><a href="styling_the_sxsw_artist_catalog.html">Styling the SXSW Artist Catalog</a></li>
      <li><a href="getting_the_most_space_on.html">Getting the most space on the marquee</a></li>
    </ul>
</div>
</div>"""

paging="""<!-- paging -->"""

index="""<!-- paging -->
<div class="paging sidebar-sect default-expanded">
<div class="sidebar-sect-title">
    <h2>Index</h2>
</div>
<div class="sidebar-sect-content">
    <ul>
        <li> <a href="entry_index.html"> Index by title </a> </li>
        <li> <a href="date_index.html"> Index by date </a> </li>
    </ul>
</div>
</div>"""

replacements = [
    ("""<h2>What I am listening to</h2>""", ""),
    ("""<object><embed src="DukeListens/support_files/user_profile_embed.swf" type="application/x-shockwave-flash" wmode="transparent" height="200" width="200"></object>""", ""),
    ("""<object><embed src="support_files/user_profile_embed.swf" type="application/x-shockwave-flash" wmode="transparent" height="200" width="200"></object>""", ""),
    ("""<h2>What I am reading</h2>""", ""),
    ("""<div class="f"><a href="https://www.google.com/reader/shared/user/07268145224739680674/state/com.google/broadcast">Google Reader »</a></div>""", ""),
    (bm, ""),
    (feeds, ""),
    (recent, ""),
    (recent2, ""),
    (paging, index),
]

def patched_text(text):
    for r in replacements:
        text = text.replace(r[0], r[1])
    return text

def patch(path):
    with open(path) as f:
        text = f.read()
        text = patched_text(text)

    with open(path, "w") as fw:
        fw.write(text)
    
if __name__ == '__main__':
    for path in sys.argv[1:]:
        patch(path)



