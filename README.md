Objective:
Build an API system to dynamically create and retrieve hierarchical categories and subcategories.
📌 Functional Requirements

 1.Create Categories & Subcategories

    i. The system should allow creating N number of unique categories.
    ii. Each category can have multiple subcategories.
    iii.Categories and subcategories must be unique by name.
    iv. Support bulk creation via API.

2.⁠ ⁠Retrieve Categories & Subcategories
        i.When a category name is provided, return:
        👉The matched category
        👉Its parent category (if exists)
        ,👉Its subcategories (children)
Limit & Pagination
  
3.⁠ ⁠If a limit parameter is provided:

    👉Return results up to the specified limit
👉If no limit is provided:
Return all results using pagination
👉Pagination should include:
page
page_size
total_count