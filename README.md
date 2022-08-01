# Anti-backup-files
This script lists backup files, uncommon documents in the repository and the usage of gitignore.

# The purpose
 So always is necessary, for the sake of security, before deploying repository content in production to check unnecessary files. Yes, this script can help you in this context to enumerate resources. Always use git ignore to prevent excessive resources.

Example how to run:
```
$ python3 anti-backup-files.py -p /home/cooler/codes/
Anti-backup-files v0.1 
 by github.com/CoolerVoid


	Usage:
	python3 anti-backup-files.py --path repository_name



List of backup files:

Path: /home/cooler/codes/chipsec/__install__/UEFI/chipsec_py368_uefi_x64.zip Size: 10.904647 MB
Path: /home/cooler/codes/codecat/Backend/application/db/data.db Size: 0.234375 MB
Path: /home/cooler/codes/codecat/doc/raptor.log Size: 0.039855 MB
Path: /home/cooler/codes/tools/test/WebGoat/src/main/resources/lessons/challenges/challenge7/git.zip Size: 0.027552 MB
Path: /home/cooler/codes/tools/test/webgoat-spring-boot-java-8/webgoat-lessons/challenge/src/main/resources/challenge7/git.zip Size: 0.027552 MB
Path: /home/cooler/codes/tools/test/pygoat/pygoat/introduction/templates/Lab/A10/debug.log Size: 0.014799 MB
Path: /home/cooler/codes/tools/test/pygoat/pygoat/app.log Size: 0.014236 MB
Path: /home/cooler/codes/codewarrior/web/syntax/media/css/.demo_page.css.swp Size: 0.011719 MB
Path: /home/cooler/codes/optionscat/config/.whitelist.conf.swp Size: 0.003906 MB
Path: /home/cooler/codes/anti-backup-files/.README.md.swp Size: 0.003906 MB
Path: /home/cooler/codes/codecat/doc/.raptor.aux.swp Size: 0.003906 MB
Path: /home/cooler/codes/codecat/doc/.beamerthemelankton-keynote.sty.swp Size: 0.003906 MB
Path: /home/cooler/codes/Rust_survival_tricks/database/Diesel_ORM/UserManagerCrud/database/test.db Size: 0.003906 MB
Path: /home/cooler/codes/tools/test/WebGoat/src/main/resources/db/container/V1__init.sql Size: 0.002424 MB
Path: /home/cooler/codes/tools/test/WebGoat/src/main/resources/lessons/sql_injection/db/migration/V2019_09_26_2__users.sql Size: 0.001338 MB
Path: /home/cooler/codes/tools/test/WebGoat/src/main/resources/lessons/sql_injection/db/migration/V2019_09_26_7__employees.sql Size: 0.000749 MB
Path: /home/cooler/codes/tools/test/WebGoat/src/main/resources/lessons/lesson_template/db/migration/V2019_11_10_1__introduction.sql Size: 0.000738 MB
Path: /home/cooler/codes/tools/test/WebGoat/src/main/resources/lessons/sql_injection/db/migration/V2019_09_26_1__servers.sql Size: 0.000713 MB
Path: /home/cooler/codes/tools/test/WebGoat/src/main/resources/lessons/sql_injection/db/migration/V2021_03_13_8__grant.sql Size: 0.000571 MB
Path: /home/cooler/codes/tools/test/WebGoat/src/main/resources/lessons/challenges/db/migration/V2018_09_26_1__users.sql Size: 0.000457 MB
Path: /home/cooler/codes/tools/test/WebGoat/src/main/resources/lessons/sql_injection/db/migration/V2019_09_26_4__tan.sql Size: 0.000452 MB
Path: /home/cooler/codes/tools/test/WebGoat/src/main/resources/lessons/sql_injection/db/migration/V2019_09_26_6__user_system_data.sql Size: 0.000439 MB
Path: /home/cooler/codes/tools/test/WebGoat/src/main/resources/lessons/sql_injection/db/migration/V2019_09_26_5__challenge_assignment.sql Size: 0.000436 MB
Path: /home/cooler/codes/tools/test/WebGoat/src/main/resources/lessons/missing_ac/db/migration/V2021_11_03_1__ac.sql Size: 0.000321 MB
Path: /home/cooler/codes/tools/test/WebGoat/src/main/resources/lessons/sql_injection/db/migration/V2019_09_26_3__salaries.sql Size: 0.000287 MB
Path: /home/cooler/codes/tools/test/WebGoat/src/main/resources/lessons/jwt/db/migration/V2019_09_25_1__jwt.sql Size: 0.000187 MB
Path: /home/cooler/codes/Rust_survival_tricks/database/Diesel_ORM/UserManagerCrud/migrations/create_users/up.sql Size: 0.000137 MB
Path: /home/cooler/codes/Rust_survival_tricks/web_service/questbook_example/migrations/2019-11-17-192300_create_tables/up.sql Size: 0.000109 MB
Path: /home/cooler/codes/tools/test/WebGoat/src/main/resources/db/container/V2__version.sql Size: 0.000055 MB
Path: /home/cooler/codes/Rust_survival_tricks/web_service/questbook_example/migrations/2019-11-17-192300_create_tables/down.sql Size: 0.000022 MB
Path: /home/cooler/codes/Rust_survival_tricks/database/Diesel_ORM/UserManagerCrud/migrations/create_users/down.sql Size: 0.000016 MB

List of documents files:

Path: /home/cooler/codes/chipsec/chipsec-manual.pdf Size: 0.829891 MB
Path: /home/cooler/codes/codecat/doc/raptor.pdf Size: 0.283712 MB
Path: /home/cooler/codes/chipsec/chipsec_tools/compression/Brotli/docs/brotli-comparison-study-2015-09-22.pdf Size: 0.205238 MB
Path: /home/cooler/codes/chipsec/build/lib/chipsec_tools/compression/Brotli/docs/brotli-comparison-study-2015-09-22.pdf Size: 0.205238 MB

List of .gitignore files:

Path: /home/cooler/codes/chipsec/chipsec_tools/log_parser/.gitignore Size: 0.001716 MB
Path: /home/cooler/codes/tools/test/WebGoat/.gitignore Size: 0.001247 MB
Path: /home/cooler/codes/tools/test/webgoat-spring-boot-java-8/.gitignore Size: 0.001114 MB
Path: /home/cooler/codes/pyspiflash/.gitignore Size: 0.000519 MB
Path: /home/cooler/codes/chipsec/.gitignore Size: 0.000485 MB
Path: /home/cooler/codes/tools/test/goat/.gitignore Size: 0.000308 MB
Path: /home/cooler/codes/tools/test/webgoat-spring-boot-java-8/webgoat-container/.gitignore Size: 0.000216 MB
Path: /home/cooler/codes/tools/test/NodeGoat/.gitignore Size: 0.000197 MB
Path: /home/cooler/codes/tools/test/pygoat/.gitignore Size: 0.000053 MB
Path: /home/cooler/codes/php-security-pitfalls/.gitignore Size: 0.000043 MB
Path: /home/cooler/codes/checksec.sh/.gitignore Size: 0.000041 MB
Path: /home/cooler/codes/optionscat/web/assets/morris.js-0.4.3/.gitignore Size: 0.000020 MB
Path: /home/cooler/codes/codecat/sandbox_of_sources/.gitignore Size: 0.000013 MB
Path: /home/cooler/codes/tools/test/webgoat-spring-boot-java-8/webgoat-lessons/cross-site-scripting/.gitignore Size: 0.000009 MB
Path: /home/cooler/codes/tools/test/webgoat-spring-boot-java-8/webgoat-lessons/vulnerable-components/.gitignore Size: 0.000009 MB

Score total

Total of possible backup files: 31
Total of possible leak of document files: 4
Total of .gitignore files: 15 



```
