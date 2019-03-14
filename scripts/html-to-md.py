# coding=utf-8

import subprocess, sys

assert(sys.argv[1].startswith("proceedings/"))
rel = ""
for i in range(2,sys.argv[1].count("/")):
  rel = rel + "../"

output = open(sys.argv[1]).read()
output = output.replace(' class="selected"', "").strip()
head = \
"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  </head>
    <body>
        <p>
            <a style="border-bottom: 0px solid #ccc;" href="https://www.modelica.org/events/modelica2019" target="_blank">
                <img src="%sstatic/images/ConferenceLogo.png" alt="Modelica 2019 Logo" width = 450 />
            </a>
        </p>
        <hr />
                        <ul>
                            <li><a href="%sindex.html">Home</a></li>
                            <li><a href="%sprogram.html">Program</a></li>
                            <li><a href="%sschedule.html">Schedule</a></li>
                            <li><a href="%ssessions.html">Sessions</a></li>
                            <li><a href="%sauthors.html">Authors</a></li>
                            <li><a href="%smaterial.html">Further material</a></li>
                        </ul>

        <hr />""" % (rel,rel,rel,rel,rel,rel,rel)

foot = \
"""<hr />
        <h2>Organized by:</h2>
        <p>
            <a style="border-bottom: 0px solid #ccc;" href="https://www.oth-regensburg.de/en.html"><img style="padding:5px;height:48px;width:auto;" src="%sstatic/images/OTHLogo.png" alt="OTH" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
            <a style="border-bottom: 0px solid #ccc;" href="http://www.modelica.org"><img style="padding:5px;height:48px;width:auto;" src="%sstatic/images/ModelicaLogo.svg" alt="Modelica" /></a>
        </p>
        <hr />
        <h2>Sponsored by:</h2>
        <p>
            <a style="border-bottom: 0px solid #ccc;" href="%sexhibitors.html">View the list of <strong>Sponsors &amp; Exhibitors</strong></a>
         </p>
    </body>
</html>""" % (rel,rel,rel)

#print(output)
#print(head)
#print(rel)

assert(head in output)
assert(foot in output)
output = output.replace(head, "").replace(foot, "")
output = output.strip()

mdfile = sys.argv[1].replace(".html",".md")
open(mdfile, "w").write(output)
subprocess.check_output(["git", "add", mdfile])
subprocess.check_output(["git", "rm", "-f", sys.argv[1]])
