# AnalystAI Project Notes

## Current Goal

Build a production-style multi-agent data analysis system that accepts uploaded CSV, Excel, and later PDF files, then produces:

- document metadata
- data quality checks
- exploratory data analysis
- statistical analysis
- visualizations
- AI business insights
- optional ML recommendations after user approval
- final report

## Architecture Summary

The system is being built in layers so each part has one responsibility.

- `app/main.py` wires the application together.
- `app/api/routes/upload.py` handles file upload requests.
- `app/services/document_service.py` creates `Document` objects.
- `app/models/document.py` stores document-level metadata.
- `app/loaders/base_loader.py` defines the loader contract.
- `app/loaders/csv_loader.py` reads CSV files.
- `app/loaders/excel_loader.py` reads Excel files.
- `app/loaders/loader_factory.py` selects the correct loader.

This separation is important because the API should stay thin, the service should own business flow, and the loaders should own file parsing.

## Key Design Decisions

- Keep the API layer thin.
- Keep business logic in the service layer.
- Keep file parsing inside loaders.
- Store internal file locations with `storage_path`.
- Return a simple success message to the user instead of exposing file paths.
- Use a unique saved filename to avoid collisions.
- Use `list` for `column_names` because it matches the natural Python structure.
- Use `Field(default_factory=list)` so each `Document` has its own list.
- Use `UploadFile` for file uploads through FastAPI.
- Use `APIRouter` for modular route organization.

## Document Model Scope

The `Document` model stores document-level metadata only:

- `document_id`
- `filename`
- `file_type`
- `storage_path`
- `upload_time`
- `file_size`
- `status`
- `row_count`
- `column_count`
- `column_names`

It should not contain:

- parsing logic
- file saving logic
- page-level PDF metadata
- analysis logic

## Current Workflow

1. User uploads a file.
2. FastAPI receives it in the upload route.
3. The route creates the `uploads/` folder if needed.
4. The file is saved with a unique name.
5. The route builds basic metadata.
6. `Document` service creates a `Document` object.
7. The API returns `File uploaded successfully`.
8. Later, the loader factory will select the correct loader.
9. The selected loader will read the file from `storage_path`.

## Why This Workflow Is Good

- Simple user experience.
- Hidden internal storage details.
- Better testability.
- Clean separation of responsibilities.
- Easy to extend later for EDA, statistics, agents, and reporting.

## End Goal Workflow

- Upload file.
- Save and register document.
- Load data with the correct loader.
- Run profiling and EDA.
- Run statistics and visualizations.
- Generate business insights.
- Ask whether ML recommendations are needed.
- If yes, run ML recommendation step.
- Generate the final report.

## Important Rule

Do not put too much logic in the API route. The route should receive the file and hand off work to services and loaders.

## Living Document Rule

This note should be updated gradually as the project grows.

- When a feature is added, update the workflow section.
- When a design decision changes, update the architecture section.
- When a new module is introduced, add it to the summary.
- Regenerate the PDF from this markdown so the docs stay in sync.