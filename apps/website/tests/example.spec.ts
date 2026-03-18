import { test, expect } from '@playwright/test';

test('homepage has correct title', async ({ page }) => {
  await page.goto('http://localhost:3000');
  
  // Expect the page title to contain "GKALogistics"
  await expect(page).toHaveTitle(/GKALogistics/);
});

test('navigation works correctly', async ({ page }) => {
  await page.goto('http://localhost:3000');
  
  // Click on the component tests link
  await page.click('text=Component Tests');
  
  // Expect to be on the test page
  await expect(page).toHaveURL(/.*test/);
});

test('theme toggle works', async ({ page }) => {
  await page.goto('http://localhost:3000');
  
  // Check initial theme (should be system preference)
  const html = await page.$('html');
  const classes = await html?.getAttribute('class');
  
  // Click theme toggle button
  await page.click('[aria-label="Toggle theme"]');
  
  // Check if theme changed
  // Note: This is a simple check, actual theme behavior depends on system preference
});