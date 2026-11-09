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

Each GEDZIP test archive in `testfiles` is built from the folder beside it: `maximal71.gdz` from `maximal71/`.
To change an archive, change the files in its folder, and for `maximal70` and `maximal71` the matching `.ged`
file too (CI checks the two agree). Don't edit the `.gdz` itself: after a pull request merges, the
"Build GEDZIP archives" workflow rebuilds it and opens a pull request with the result. To build them locally, run
`python3 .github/scripts/build_gdz.py`.

Why: an archive is a binary file, and Git can't merge two changes to one, so when two open pull requests both edited
an archive, merging one made the other conflict. Building archives from their folders means pull requests change only
text files, which Git merges.
