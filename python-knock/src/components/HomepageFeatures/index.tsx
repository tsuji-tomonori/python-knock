import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  description: JSX.Element;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Python 基礎',
    description: (
      <>
        変数、データ型、制御構造などの基本を学ぶ問題を解こう！
      </>
    ),
  },
  {
    title: 'アルゴリズム',
    description: (
      <>
        ソートや探索アルゴリズムを実装して、理解を深めよう。
      </>
    ),
  },
  {
    title: 'データ構造',
    description: (
      <>
        スタック、キュー、木構造など、実践的なデータ構造を学ぼう！
      </>
    ),
  },
];

function Feature({ title, description }: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className={styles.featureCard}>
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): JSX.Element {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
