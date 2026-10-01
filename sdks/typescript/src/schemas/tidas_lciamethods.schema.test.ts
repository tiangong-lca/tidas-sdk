import assert from 'node:assert/strict';
import { describe, it } from 'node:test';
import { LciamethodsSchema } from './tidas_lciamethods.schema';

function reviewSchema() {
  return (LciamethodsSchema as any).shape.LCIAMethodDataSet.shape
    .modellingAndValidation.shape.validation.shape.review;
}

const localizedText = { '@xml:lang': 'en', '#text': 'Reviewed documentation' };
const reference = (type: 'contact data set' | 'source data set') => ({
  '@type': type,
  '@refObjectId': type === 'contact data set'
    ? '11111111-1111-1111-1111-111111111111'
    : '22222222-2222-2222-2222-222222222222',
  '@version': '01.00.000',
  '@uri': type === 'contact data set'
    ? '../contacts/11111111-1111-1111-1111-111111111111.xml'
    : '../sources/22222222-2222-2222-2222-222222222222.xml',
  'common:shortDescription': localizedText,
});

const completedReview = {
  '@type': 'Independent external review',
  'common:scope': {
    '@name': 'Documentation',
    'common:method': { '@name': 'Expert judgement' },
  },
  'common:reviewDetails': localizedText,
  'common:referenceToNameOfReviewerAndInstitution': reference('contact data set'),
};

describe('LCIA method review conditional schema', () => {
  it('accepts an omitted or valid report reference and rejects an incomplete one', () => {
    const schema = reviewSchema();
    assert.strictEqual(schema.safeParse(completedReview).success, true);
    assert.strictEqual(
      schema.safeParse({
        ...completedReview,
        'common:referenceToCompleteReviewReport': reference('source data set'),
      }).success,
      true
    );
    assert.strictEqual(
      schema.safeParse({
        ...completedReview,
        'common:referenceToCompleteReviewReport': {
          '@refObjectId': '22222222-2222-2222-2222-222222222222',
        },
      }).success,
      false
    );
  });

  it('keeps the other completed-review evidence required', () => {
    const result = reviewSchema().safeParse({ '@type': 'Independent external review' });
    assert.strictEqual(result.success, false);
    if (!result.success) {
      assert.deepStrictEqual(
        result.error.issues.map((issue: any) => issue.path.join('.')).sort(),
        [
          '',
          'common:referenceToNameOfReviewerAndInstitution',
          'common:reviewDetails',
        ]
      );
    }
  });
});
