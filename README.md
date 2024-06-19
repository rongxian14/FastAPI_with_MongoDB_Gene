## Gene Expression API

This API allows you to interact with gene expression data stored in a MongoDB database. Below are the available endpoints:

### 1. Home

**Endpoint**: `GET /`

**Description**: 
- A simple welcome message to the Gene Expression API.

**Response**:
```json
{
  "message": "Welcome to the Gene Expression API",
  "done": "by Lee Rong Xian A21EC0043"
}
```

### 2. Retrieve All Gene IDs

**Endpoint**: `GET /gene/`

**Description**: 
- Retrieves a list of all Gene IDs available in the database.

### 3. Retrieve Information About a Specific Gene

**Endpoint**: `GET /gene/{gene_id}`

**Description**: 
- Retrieves all information about a specific gene by its Gene ID.

**Path Parameters**:
- `gene_id`: The ID of the gene to retrieve information for.

**Response**:
```json
{
  "Gene_ID": "Gene_ID_1",
  "Gene_Name": "Gene_Name_1",
  "Chromosome": "chr1",
  "Start_Position": 123456,
  "End_Position": 789012,
  "expression": [
    {
      "Sample_ID": "Sample_ID_1",
      "Expression_Level": 12.34,
      "Condition": "Condition_1"
    },
    ...
  ],
  "sample": [
    {
      "Sample_ID": "Sample_ID_1",
      "Patient_ID": "Patient_ID_1",
      "Collection_Date": "2023-01-01",
      "Condition": "Condition_1",
      "Tissue_Type": "Tissue_Type_1"
    },
    ...
  ]
}
```

### 4. Retrieve Expression Data for a Specific Gene Across All Samples

**Endpoint**: `GET /gene/{gene_id}/expression`

**Description**: 
- Retrieves the expression data for a specific gene across all samples.

**Path Parameters**:
- `gene_id`: The ID of the gene to retrieve expression data for.

**Response**:
```json
{
  "expression": [
    {
      "Sample_ID": "Sample_ID_1",
      "Expression_Level": 12.34,
      "Condition": "Condition_1"
    },
    ...
  ]
}
```

### 5. Retrieve All Sample Information for a Specific Patient

**Endpoint**: `GET /patient/{patient_id}/samples`

**Description**: 
- Retrieves all sample information for a specific patient.

**Path Parameters**:
- `patient_id`: The ID of the patient to retrieve sample information for.

**Response**:
```json
{
  "sample": [
    {
      "Sample_ID": "Sample_ID_1",
      "Patient_ID": "Patient_ID_1",
      "Collection_Date": "2023-01-01",
      "Condition": "Condition_1",
      "Tissue_Type": "Tissue_Type_1"
    },
    ...
  ]
}
```

You can copy this content into your `README.md` file to document the endpoints of your API. This should help users understand how to interact with your API and what kind of data to expect from each endpoint.
