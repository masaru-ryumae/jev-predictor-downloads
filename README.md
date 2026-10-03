# College Admissions Predictor, Jev API Files

From The Engineering Dad, "You Do Not Need To Know How To Code To Build A College Admissions Predictor Tonight"

https://theengineeringdad.substack.com/p/the-easiest-first-build

The free section walks through the five-minute version, no code required. The paid section explains what the fields below mean, how the Common Data Set parsing actually works, and the real problems hit building this (a wording variant between schools, a fillable-form trap, a false-positive bug that silently returned fake data for one school before it got caught). That context is what makes these three files actually usable rather than just code that runs.

## Files

- **call_jev.py**, calls the real TypeSafe Jev API directly. Needs your own API key in a local `.env` file (`TYPESAFE_API_KEY=your-key-here`), never put it in the script itself, never commit it.
- **request_template.json**, the file call_jev.py reads. Pre-filled with the example applicant from the article. Replace the `applicant_profile` values with your own kid's numbers, replace `institution_benchmark` with a school's entry from the file below.
- **21_school_benchmarks.json**, real Common Data Set admissions data (2025-26 cycle) for 21 schools, already pulled and parsed, ready to paste in.

## Quick start

```bash
pip install requests python-dotenv
echo "TYPESAFE_API_KEY=your-key-here" > .env
python call_jev.py request_template.json
```

Edit `request_template.json` first with your own applicant and school before running it for real, the version as shipped is the example from the article.
