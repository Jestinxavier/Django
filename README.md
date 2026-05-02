## Objective
Build an API system to dynamically create and retrieve hierarchical categories and subcategories.

## Functional Requirements
1. Create categories and subcategories.
2. Enforce unique names for categories/subcategories.
3. Support bulk creation via API.
4. Retrieve category tree data (parent and children).
5. Support listing with limit/pagination.

## API Routes
- `GET /categories/` - List categories (supports pagination and limit).
- `POST /categories/` - Add category/subcategory.
- `POST /categories/bulk-import/` - Bulk import nested category data.

## Listing With Pagination
- If `limit` is provided, API returns up to the specified number of records.
- If `limit` is not provided, API returns paginated results.
- Pagination response includes:
- `page`
- `page_size`
- `total_count`

## Screenshots
### Category Listing + Pagination
![Category Listing + Pagination](https://res.cloudinary.com/dtwj3t1s2/image/upload/v1777717368/Screenshot_2026-05-02_at_3.42.52_PM_tw4iv1.png)

### Category Add
![Category Add](https://res.cloudinary.com/dtwj3t1s2/image/upload/v1777717368/Screenshot_2026-05-02_at_3.45.33_PM_e0h2sp.png)

### Bulk Import
![Bulk Import](https://res.cloudinary.com/dtwj3t1s2/image/upload/v1777717368/Screenshot_2026-05-02_at_3.49.22_PM_rlbpvl.png)

## Sample Data For Bulk Import
```json
[
  {
    "name": "Electronics",
    "children": [
      {
        "name": "Mobiles",
        "children": [
          { "name": "Samsung" },
          { "name": "Apple" },
          { "name": "OnePlus" }
        ]
      },
      {
        "name": "Laptops",
        "children": [
          { "name": "Dell" },
          { "name": "HP" },
          { "name": "Lenovo" }
        ]
      }
    ]
  },
  {
    "name": "Fashion",
    "children": [
      {
        "name": "Men",
        "children": [
          { "name": "Shirts" },
          { "name": "Jeans" },
          { "name": "Shoes" }
        ]
      },
      {
        "name": "Women",
        "children": [
          { "name": "Sarees" },
          { "name": "Handbags" },
          { "name": "Footwear" }
        ]
      }
    ]
  },
  {
    "name": "Home Appliances",
    "children": [
      {
        "name": "Kitchen",
        "children": [
          { "name": "Mixer" },
          { "name": "Microwave" }
        ]
      },
      {
        "name": "Cleaning",
        "children": [
          { "name": "Vacuum Cleaner" },
          { "name": "Washing Machine" }
        ]
      }
    ]
  }
]
```
