# AutoGrade  
**Automated MCQ Grading with Computer Vision and Optical Mark Recognition (OMR) Technology** ✅  

<img width="462" alt="Screenshot 2024-12-23 at 09 07 22" src="https://github.com/user-attachments/assets/a8ab266e-e6e8-4e93-91b2-af9517f4d3fa" />

<img width="462" alt="Screenshot 2024-12-23 at 09 07 34" src="https://github.com/user-attachments/assets/6709949b-8e2b-422f-9f53-cc3d1ce19e4a" />

### Overview  
AutoGrade is a smart solution to grade multiple-choice questions (MCQs) automatically. It uses computer vision and Optical Mark Recognition (OMR) to make grading faster and more accurate, saving time and reducing errors.


### Key Features  
- **Smart Image Analysis**: Detects and checks marked answers with image processing.  
- **Precise Recognition**: Finds and reads filled bubbles or checkboxes accurately.  
- **Handles Many Sheets**: Grades multiple answer sheets at once.  
- **Flexible Designs**: Works with different types of answer sheet layouts.  
- **Quick Results**: Gives instant scores and useful feedback.

### Technology Stack  
- **Programming Language**: Python  
- **Libraries**:  
  - OpenCV for processing images  
  - NumPy for calculations  
  - Pandas for organizing data  
- **Backend**: FastAPI for APIs and app setup  
- **Testing**: PyTest for checking code quality  

### Challenges Solved  
- Reduces mistakes from manual grading  
- Speeds up the grading process  
- Handles large numbers of answer sheets efficiently  

### Outcome  
AutoGrade makes grading easy and accurate, helping teachers and examiners save time and focus on other tasks.

---

## Approach  

### 1. Image Preprocessing  
- Load and resize the input image for consistent analysis.  
- Convert to grayscale to simplify the image.  
- Apply blur to reduce noise.  
- Detect edges with the Canny edge detector.  

### 2. Finding Rectangles  
- Find all contours (shapes) in the image.  
- Select rectangle shapes based on size and structure.  
- Sort the rectangles by size and pick the important ones.  

### 3. Fixing the View  
- Get the corners of each rectangle.  
- Use perspective transformation to view the rectangle flat like a paper.  
- Crop to keep only the part with answers.  

### 4. Recognizing Marks  
- Change each cropped rectangle to grayscale.  
- Use binary thresholding to highlight the marks.  
- Check the density of pixels to see which answers are filled.  

### 5. Showing Results  
- Use a Tkinter window to show all steps and results in one place.  

### 6. Tools and Functions  
- Functions to find rectangles and order their corners.  
- Tools to filter and display images step by step.  

---

### Contact  
For more details, feel free to reach out via email or connect on LinkedIn.  
