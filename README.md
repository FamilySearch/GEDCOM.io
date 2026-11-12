# GEDCOM.io website

This project contains the files for the GEDCOM.io website. It has been created using Jekyll and the Minimal Mistakes theme.

## Running the website locally

In order to run this website for development purposes, do the following on your development machine.

1. [Setup Jekyll](https://jekyllrb.com/docs/).
2. Clone this repository into desired directory.
3. From the project directory, run the following command
```bash
bundle install
```
4. Run the project
```bash
bundle exec jekyll serve -w --config _config.yml,_config.dev.yml
```

## Test files

Each GEDZIP test archive in `testfiles` has a folder beside it with the same files: `maximal71.gdz` and `maximal71/`.
The folder is there so a change can be reviewed, since GitHub can't show what changed inside an archive.

To change an archive:

1. Change the files in its folder, and for `maximal70` and `maximal71` the matching `.ged` file too.
2. Run `python3 testfiles/build_gdz.py` from the repository's root. It rebuilds each archive whose folder changed.
3. Commit the folder, the `.ged` file and the `.gdz` together.

The pull request's checks confirm that the archive and its folder hold the same files with the same bytes, and that
the `.ged` file and the archive's `gedcom.ged` agree, so every commit on `main` has them in step.

If another pull request that changed the same archive merges first, yours will conflict on the `.gdz`, because Git
can't merge two changes to a binary file. Merge `main` into your branch, keep both changes in the folder and the
`.ged` file, run the script again, and commit the archive it builds.
