const request = require('supertest');
const app = require('../src/server');
const db = require('../src/db');

describe('Integration Tests', () => {
  afterAll(async () => {
    await db.end();
  });

  it('GET /health should return 200 and DB time', async () => {
    const res = await request(app).get('/health');
    expect(res.statusCode).toEqual(200);
    expect(res.body).toHaveProperty('status', 'ok');
    expect(res.body).toHaveProperty('time');
  });
});
