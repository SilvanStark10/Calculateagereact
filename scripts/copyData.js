const fs = require('fs');
const path = require('path');

// Define paths
const srcPath = path.join(__dirname, '../public/data/life_expectancy_data.csv');
const destDir = path.join(__dirname, '../build/data');
const destPath = path.join(destDir, 'life_expectancy_data.csv');

// Function to check if file exists
function checkFileExists(filePath) {
  if (!fs.existsSync(filePath)) {
    console.error(`Error: File not found: ${filePath}`);
    console.error('Please ensure the life_expectancy_data.csv file exists in the public/data directory.');
    return false;
  }
  return true;
}

// Create directory if it doesn't exist
try {
  if (!fs.existsSync(destDir)) {
    console.log(`Creating directory: ${destDir}`);
    fs.mkdirSync(destDir, { recursive: true });
  }

  // Check if source file exists before attempting to copy
  if (!checkFileExists(srcPath)) {
    process.exit(1);
  }

  // Copy the file
  console.log(`Copying file from ${srcPath} to ${destPath}`);
  fs.copyFileSync(srcPath, destPath);
  console.log('File copied successfully');
} catch (err) {
  console.error('Error during file operations:', err);
  process.exit(1);
} 