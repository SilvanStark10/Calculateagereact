const fs = require('fs');
const path = require('path');

// Define paths
const srcPath = path.join(__dirname, '../public/data/life_expectancy_data.csv');
const destDir = path.join(__dirname, '../build/data');
const destPath = path.join(destDir, 'life_expectancy_data.csv');

// Create directory if it doesn't exist
if (!fs.existsSync(destDir)) {
  console.log(`Creating directory: ${destDir}`);
  fs.mkdirSync(destDir, { recursive: true });
}

// Copy the file
try {
  console.log(`Copying file from ${srcPath} to ${destPath}`);
  fs.copyFileSync(srcPath, destPath);
  console.log('File copied successfully');
} catch (err) {
  console.error('Error copying file:', err);
  process.exit(1);
} 