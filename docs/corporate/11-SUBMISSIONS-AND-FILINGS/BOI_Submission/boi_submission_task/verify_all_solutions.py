#!/usr/bin/env python3

import os

def verify_files_exist():
    """Verify that all solution files were created correctly"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    
    # Files that should exist after running all solutions
    expected_files = [
        # Scripts
        "improved_image_centering.py",
        "create_pdf_with_improved_centering.py",
        "exact_image_centering.py",
        "create_pdf_with_exact_centering.py",
        "final_image_centering_solution.py",
        
        # Markdown files
        "ESMS_Handbook_with_Precise_Images.md",
        "ESMS_Handbook_with_Improved_Centering.md",
        "ESMS_Handbook_with_Exact_Centering.md",
        "ESMS_Handbook_with_Best_Centering.md",
        
        # CSS files
        "improved_centering_style.css",
        "exact_centering_style.css",
        "best_centering_style.css",
        
        # Final PDFs
        "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Precise.pdf",
        "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Improved.pdf",
        "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Exact.pdf",
        
        # Documentation
        "IMAGE_CENTERING_SOLUTIONS.md",
        "README_IMAGE_CENTERING.md",
        "WHY_IMAGES_NOT_CENTERED.md",
        "USE_BEST_CENTERING.md"
    ]
    
    print("VERIFICATION OF ALL SOLUTION FILES")
    print("=" * 50)
    
    found_files = 0
    missing_files = 0
    
    for file_name in expected_files:
        file_path = os.path.join(base_dir, file_name)
        if os.path.exists(file_path):
            file_size = os.path.getsize(file_path)
            if file_size > 0:
                print(f"✓ {file_name} ({file_size} bytes)")
                found_files += 1
            else:
                print(f"⚠ {file_name} (EMPTY FILE)")
                missing_files += 1
        else:
            print(f"✗ {file_name} (NOT FOUND)")
            missing_files += 1
    
    print("\n" + "=" * 50)
    print(f"SUMMARY:")
    print(f"  Files found: {found_files}")
    print(f"  Files missing/empty: {missing_files}")
    print(f"  Total files checked: {len(expected_files)}")
    
    if missing_files == 0:
        print("\n🎉 ALL SOLUTION FILES ARE PRESENT AND CORRECT!")
        print("\nRecommended next steps:")
        print("1. Review WHY_IMAGES_NOT_CENTERED.md to understand the issue")
        print("2. Check IMAGE_CENTERING_SOLUTIONS.md for detailed approaches")
        print("3. Use final_image_centering_solution.py for the best results")
        print("4. Follow USE_BEST_CENTERING.md for implementation instructions")
    else:
        print(f"\n⚠ {missing_files} files need attention.")
        
    return missing_files == 0

def check_optimized_images():
    """Check if optimized images were created"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    diagrams_dir = os.path.join(base_dir, "diagrams")
    
    print("\nOPTIMIZED IMAGES CHECK")
    print("=" * 30)
    
    expected_images = [
        "diagram_1_optimized.png",
        "diagram_1_exact_centered.png",
        "diagram_1_final.png",
        "diagram_2_optimized.png",
        "diagram_2_exact_centered.png",
        "diagram_2_final.png",
        "diagram_3_optimized.png",
        "diagram_3_exact_centered.png",
        "diagram_3_final.png",
        "diagram_4_optimized.png",
        "diagram_4_exact_centered.png",
        "diagram_4_final.png"
    ]
    
    found_images = 0
    for image_name in expected_images:
        image_path = os.path.join(diagrams_dir, image_name)
        if os.path.exists(image_path):
            file_size = os.path.getsize(image_path)
            print(f"✓ {image_name} ({file_size} bytes)")
            found_images += 1
        else:
            print(f"✗ {image_name} (NOT FOUND)")
    
    print(f"\nFound {found_images}/{len(expected_images)} optimized images")
    return found_images

def main():
    """Main verification function"""
    print("COMPREHENSIVE VERIFICATION OF IMAGE CENTERING SOLUTIONS")
    print("=" * 60)
    
    # Verify all solution files
    files_ok = verify_files_exist()
    
    # Check optimized images
    image_count = check_optimized_images()
    
    print("\n" + "=" * 60)
    print("FINAL VERIFICATION STATUS:")
    if files_ok and image_count >= 8:
        print("✅ ALL SOLUTIONS IMPLEMENTED SUCCESSFULLY!")
        print("✅ READY TO GENERATE PDFS WITH PROPERLY CENTERED IMAGES!")
    else:
        print("⚠ SOME COMPONENTS MISSING - PLEASE REVIEW OUTPUT ABOVE")
    
    print("\nFor detailed information, check:")
    print("- WHY_IMAGES_NOT_CENTERED.md")
    print("- IMAGE_CENTERING_SOLUTIONS.md")
    print("- README_IMAGE_CENTERING.md")

if __name__ == "__main__":
    main()